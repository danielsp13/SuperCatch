FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"

# Crear usuario sin privilegios
RUN useradd -m lyoko

# Establecer directorio de trabajo para test
RUN mkdir -p /app/test && \
    chown lyoko --recursive /app

# Trabajar con usuario sin privilegios
USER lyoko

# Configurar variables de entorno
ENV HOME="/home/lyoko"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"

# Especificar directorio de trabajo
WORKDIR /app/test

# Copiar archivos necesarios
COPY --chown=lyoko poetry.lock pyproject.toml requirements.txt ./

# Instalar dependencias y eliminar ficheros no necesarios
RUN pip install -r requirements.txt --no-cache-dir && \
    poe install && \
    poe nltk_data && \
    rm ./poetry.lock ./pyproject.toml ./requirements.txt && \
    rm ${HOME}/nltk_data/corpora/stopwords.zip && \
    find ${HOME}/nltk_data/corpora/stopwords -type f -not -name 'spanish' -delete

# Especificar punto de entrada
ENTRYPOINT ["poe", "test"]
