FROM python:latest
WORKDIR /app
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install telebot

COPY app.py run.sh ./
ENTRYPOINT ["python", "app.py"]

