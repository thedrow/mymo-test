FROM python:3.6-alpine

RUN pip install -U pip setuptools wheel pipenv
RUN apk update && apk add postgresql-dev build-base && rm -rf /var/cache/apk/*

COPY . /src
WORKDIR /src

RUN pipenv install --system --deploy
