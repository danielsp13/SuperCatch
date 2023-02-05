FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"

ARG the_runner="lyoko"

# Crear usuario sin privilegios
RUN useradd -m $the_runner

# Establecer directorio de trabajo para test
RUN mkdir -p /app/test && \
    chown $the_runner --recursive /app

# Trabajar con usuario sin privilegios
USER $the_runner

# Configurar variables de entorno
ENV HOME="/home/$the_runner"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"

# Especificar directorio de trabajo
WORKDIR $HOME

# Copiar archivos necesarios
COPY --chown=$the_runner poetry.lock pyproject.toml requirements.txt ./

# Tratar pyproject para convertir a requirements
RUN sed -i "`cat pyproject.toml | grep "poetry.*.dependencies" | grep -v "poetry.dependencies" | tr -d '[]' | sed -e 's/^/\//' -e 's/$/\/d/' -e '1 s/$/;/' | xargs | sed 's/ //'`" ./pyproject.toml 

# Instalar dependencias y eliminar ficheros no necesarios
RUN pip install `cat requirements.txt | grep poetry` --no-cache-dir &&\
    sed -i "/poetry/d" ./requirements.txt &&\
    poetry config virtualenvs.create false && \
    poetry lock --no-update && \   
    poetry export -f requirements.txt --without-hashes >> requirements.txt &&\
    pip install -r requirements.txt --no-cache-dir &&\
    poe nltk_data && \
    rm ./poetry.lock ./pyproject.toml ./requirements.txt && \
    rm ${HOME}/nltk_data/corpora/stopwords.zip && \
    find ${HOME}/nltk_data/corpora/stopwords -type f -not -name 'spanish' -delete
    
WORKDIR /app/test

# Especificar punto de entrada
ENTRYPOINT ["poe","test"]
