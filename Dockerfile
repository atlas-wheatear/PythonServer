FROM python:3.8

WORKDIR /usr/src/app

COPY requirements/production.txt requirements.txt

RUN pip install -r requirements.txt

COPY pythonserver/ .

CMD python -m server
