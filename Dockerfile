FROM python:3.11

WORKDIR /music_bot

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "bot.py"]