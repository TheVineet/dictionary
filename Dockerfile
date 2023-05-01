FROM python:latest

WORKDIR /home/dictionary

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app .

CMD [ "python", "./app.py" ]