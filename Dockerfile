FROM python:3.6-alpine

RUN pip install -U pip setuptools wheel pipenv

COPY . /src
WORKDIR /src

RUN apk update && apk add postgresql-dev build-base && rm -rf /var/cache/apk/*
RUN pipenv install --system --deploy
