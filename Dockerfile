FROM python:slim

LABEL maintainer="danielperezruiz.10@gmail.com" \
      version="0.0.5"
      
RUN useradd -m supercatch

RUN mkdir -p /app/test && \
    chown supercatch --recursive /app

ENV HOME="/home/supercatch"
ENV POETRY_HOME="$HOME/.local/poetry"
ENV PATH="${POETRY_HOME}/bin:$PATH:${HOME}/.local/bin"

WORKDIR /app/test

USER supercatch

COPY --chown=supercatch poetry.lock pyproject.toml ./

RUN pip install poetry poethepoet --no-cache-dir &&\
    poe install &&\
    poe nltk_data && \
    rm ./poetry.lock ./pyproject.toml && \
    rm ${HOME}/nltk_data/corpora/stopwords.zip && \
    rm ${HOME}/nltk_data/corpora/stopwords/*[^spanish]*

ENTRYPOINT ["poe","test"]
