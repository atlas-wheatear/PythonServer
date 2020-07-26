# Python Server

This is a project for me to learn best practices regarding _flask_ applications running in _docker_ containers.

## Installing Development Dependencies

For pip development dependencies:

`pip install -r requirements/development.txt`

The chrome and firefox browsers are required, alongisde their respective webdrivers.

## Configuring

Copy the contents of **postgres_example.env** into **postgres.env**, e.g. on _linux_:

`cp postgres_example.env postgres.env`

Edit the password entry to a secure password, without enclosing in quotation marks.

## Building and Running

`docker-compose up`
