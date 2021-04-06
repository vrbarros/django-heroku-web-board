FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gettext libgettextpo-dev postgresql-client

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
