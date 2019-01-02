FROM python:3.7.1-alpine3.8

WORKDIR /app

RUN apk update --no-cache && apk add --no-cache postgresql-dev gcc python3-dev musl-dev && pip install pipenv

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv install

COPY . /app

ENV FLASK_APP main
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

CMD pipenv run createdb && pipenv run start-dev
