FROM python:3.8

WORKDIR /usr/src/app

COPY requirements/production.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY pythonserver/ pythonserver/

COPY database/postgres.env pythonserver/.env

CMD python -um pythonserver.server
