FROM python:3.6-slim-stretch
RUN apt-get update && apt-get -y install gcc

COPY requirements.dev.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./sanic_mongodb_ext /app/sanic_mongodb_ext
COPY ./LICENSE /app
COPY ./README.rst /app
COPY ./setup.py /app
WORKDIR /app

RUN python setup.py develop
