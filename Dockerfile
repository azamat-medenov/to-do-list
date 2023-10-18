FROM python:3.12 as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    PYTHONPATH=/app
RUN mkdir app
WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /app/

RUN pip3 install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .


