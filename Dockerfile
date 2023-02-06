FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"
      
# Crear usuario sin privilegios
RUN useradd -m lyoko

# Establecer directorio de trabajo para test
RUN mkdir -p /app/test && \
    chown lyoko --recursive /app

# Configurar variables de entorno
ENV HOME="/home/lyoko"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV POETRY_VENV_DIR="$HOME/.cache/pypoetry/virtualenvs"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"

# Especificar directorio de trabajo
WORKDIR /app/test

# Trabajar con usuario sin privilegios
USER lyoko

# Copiar archivos necesarios
COPY --chown=lyoko poetry.lock pyproject.toml ./

# Instalar dependencias y eliminar ficheros no necesarios
RUN pip install poetry poethepoet &&\
    poe install &&\
    poe nltk_data && \
    rm ./poetry.lock ./pyproject.toml && \
    rm ${HOME}/nltk_data/corpora/stopwords.zip && \
    find ${HOME}/nltk_data/corpora/stopwords -type f -not -name 'spanish' -delete

# Especificar punto de entrada
ENTRYPOINT ["poe","test"]
