FROM python:3.9

WORKDIR /blog

COPY . .
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
