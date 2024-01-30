FROM python:3.8-slim-buster

WORKDIR /app

LABEL org.opencontainers.image.source https://github.com/marceloalmeida/slack-last-message-fetcher

ADD main.py requirements.txt /app

RUN \
    pip install --no-cache-dir -r requirements.txt

CMD ["./main.py"]
