FROM python:3.8.2-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y gettext 
