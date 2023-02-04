FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"

# Crear usuario sin privilegios
RUN useradd -m lyoko

# Trabajar con usuario sin privilegios
USER lyoko

# Configurar variables de entorno
ENV HOME="/home/lyoko"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"
