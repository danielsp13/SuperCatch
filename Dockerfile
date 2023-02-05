# ---- Fase de construcción
FROM python:slim as builder

ARG poetry_dev_dependencies="\[tool.poetry.dev-dependencies\]"
ARG poetry_test_dependencies="\[tool.poetry.group.test.dependencies\]"
ARG the_builder="bob"

# Crear usuario sin privilegios
RUN useradd -m $the_builder

# Configurar variables de entorno
ENV HOME_BUILDER="/home/$the_builder"
ENV POETRY_HOME="${HOME_BUILDER}/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME_BUILDER}/.local/bin"

WORKDIR $HOME_BUILDER

# Usuario trabajador
USER $the_builder

# Copiar archivos necesarios
COPY --chown=$the_builder poetry.lock pyproject.toml requirements.txt ./

# Tratar pyproject para convertir a requirements
RUN sed -i "/$poetry_dev_dependencies/d" ./pyproject.toml &&\
    sed -i "/$poetry_test_dependencies/d" ./pyproject.toml

# Instalar poetry y obtener requirements
RUN pip install `cat requirements.txt | grep poetry` --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry lock --no-update && \   
    poetry export -f requirements.txt --without-hashes >> requirements.txt


# ========================================================================

# ---- Fase final
FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"

ARG the_runner="lyoko"
ARG the_home_builder="/home/bob"

# Crear usuario sin privilegios
RUN useradd -m $the_runner

# Establecer directorio de trabajo para test
RUN mkdir -p /app/test && \
    chown lyoko --recursive /app

# Trabajar con usuario sin privilegios
USER $the_runner

# Configurar variables de entorno
ENV HOME="/home/$the_runner"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"

# Especificar directorio de trabajo
WORKDIR $HOME

# Copiar archivos necesarios
COPY --from=builder --chown=lyoko $the_home_builder/pyproject.toml $the_home_builder/requirements.txt ./

# Instalar dependencias y eliminar ficheros no necesarios
RUN pip install -r requirements.txt --no-cache-dir && \
	poetry config virtualenvs.create false && \
    poe nltk_data && \
    rm ./pyproject.toml ./requirements.txt && \
    rm ${HOME}/nltk_data/corpora/stopwords.zip && \
    find ${HOME}/nltk_data/corpora/stopwords -type f -not -name 'spanish' -delete
    
WORKDIR /app/test

# Especificar punto de entrada
ENTRYPOINT ["poe","test"]
