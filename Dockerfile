FROM python:3.8

WORKDIR /usr/src/app

COPY requirements/production.txt requirements.txt

RUN pip install -r requirements.txt

COPY config.toml .

EXPOSE 5000

COPY pythonserver/ pythonserver/

CMD python -um pythonserver.server
