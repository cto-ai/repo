FROM registry.cto.ai/official_images/python:latest

WORKDIR /ops

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
