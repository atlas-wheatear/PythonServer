#!/bin/bash

python database/env.py
docker-compose build
docker-compose up
