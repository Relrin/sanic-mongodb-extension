FROM python:3.11-slim-bullseye
RUN apt-get update && apt-get -y install gcc

RUN pip install --upgrade pip
COPY requirements.dev.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./sanic_mongodb_ext /app/sanic_mongodb_ext
COPY ./LICENSE /app
COPY ./README.rst /app
COPY ./setup.py /app
WORKDIR /app

RUN python setup.py develop
