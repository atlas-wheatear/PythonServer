import toml

def load_config():
    config = toml.load("config.toml")
    return config

def build_env():
    env_file = open("postgres.env", "w")
    config = load_config()
    for key, value in config.items():
        if key in ("POSTGRES_PORT", "POSTGRES_HOSTNAME"):
            continue
        env_file.write("{}={}\n".format(key, value.strip("\"")))
    env_file.close()

build_env()
