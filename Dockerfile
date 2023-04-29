FROM python:3.11-slim
ARG REQUIREMETS
ENV PYTHONNUNBUFFERED 1
WORKDIR /code
COPY . .
RUN pip install -r /code/requirements.txt
