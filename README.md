# Python Server

This is a project for me to learn best practices regarding _flask_ applications running in _docker_ containers.

## Installing Development Dependencies

For pip development dependencies:

`pip install -r requirements/development.txt`

The chrome and firefox browsers are required, alongisde their respective webdrivers.

## Configuring

Copy the contents of the file **postgres.env.dist** from the **config** directory into a file (in the root directory) named **postgres.env**, e.g. on _linux_:

`cp configs/postgres.env.dist postgres.env`

Uncomment the _POSTGRES\_PASSWORD_ entry and edit it to contain a secure password, without any spaces and without enclosing in quotation marks. Do the same into **config.toml** from **config.toml.dist**:

`cp configs/config.toml.dist config.toml`

Uncomment and edit the _POSTGRES\_PASSWORD_ entry to be the _same_ password_ as before. This config duplication is far from ideal, and will be _refactored_ in future.

## Testing

Run the following command from the root directory:

`pytest`

## Building and Running

`docker-compose up`
