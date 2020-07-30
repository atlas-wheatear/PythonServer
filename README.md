# Python Server

This is a project for me to learn best practices regarding _flask_ applications running in _docker_ containers.

## Installing Development Dependencies

For pip development dependencies:

`pip install -r requirements/development.txt`

The chrome and firefox browsers are required, alongisde their respective webdrivers.

## Configuring

Copy the contents of the file **postgres.env.dist** from the **database** directory into a file named **postgres.env** within the _same_ directory, e.g. on _linux_:

`cp database/postgres.env.dist database/postgres.env`

Uncomment the _POSTGRES\_PASSWORD_ entry and edit it to contain a secure password, without any spaces and without enclosing in quotation marks.

## Testing

Run the following command from the root directory:

`pytest`

## Building and Running

To build:

`docker-compose build`

To run:

`docker-compose up`
