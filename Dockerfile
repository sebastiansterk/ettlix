FROM python:3.9-alpine3.17
WORKDIR /app

RUN apk update && apk upgrade && pip install --upgrade pip
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install telebot

COPY app.py .
ENTRYPOINT ["python", "app.py"]

