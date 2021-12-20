FROM python:3.10-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python3 ./run.py
