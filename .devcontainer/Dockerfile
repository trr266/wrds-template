FROM python:3.12-slim

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src .

