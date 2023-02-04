FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"

# Crear usuario sin privilegios
RUN useradd -m lyoko

# Trabajar con usuario sin privilegios
USER lyoko
