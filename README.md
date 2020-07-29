# Python Server

This is a project for me to learn best practices regarding _flask_ applications running in _docker_ containers.

## Installing Development Dependencies

For pip development dependencies:

`pip install -r requirements/development.txt`

The chrome and firefox browsers are required, alongisde their respective webdrivers.

## Configuring

Copy the contents of the file **postgres.env.dist** from the **config** directory into a file (in the root directory) named **postgres.env**, e.g. on _linux_:

`cp configs/postgres.env.dist postgres.env`

Edit the _POSTGRES\_PASSWORD_ entry to a secure password, without any spaces and without enclosing in quotation marks. Do for the same into **config.toml** from **config.toml.dist**:

`cp configs/config.toml.dist config.toml`

Edit the _POSTGRES\_PASSWORD_ entry to be the _same_ password_ as before. This config duplication is far from ideal, and will be refactored in future.

## Testing

Run the following command from the root directory:

`pytest`

## Building and Running

`docker-compose up`
