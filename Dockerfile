FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY . .

RUN pip install -r ./requirements.txt

ENV FLASK_APP app.py

CMD python app.py
