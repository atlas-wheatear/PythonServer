@echo off

python database/env.py
docker-compose build
docker-compose up
