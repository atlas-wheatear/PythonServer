import toml
import psycopg2
import sys

class Model():
    def load_config(self):
        config = toml.load("config.toml")
        return config
    
    def connect(self, config):
        connection = psycopg2.connect(
            user = config["POSTGRES_USER"],
            host = config["POSTGRES_HOSTNAME"],
            port = str(config["POSTGRES_PORT"]),
            dbname = config["POSTGRES_DB"],
            password = config["POSTGRES_PASSWORD"]
        )
        return connection
    
    def close(self):
        if (self.connection):
            self.cursor.close()
            self.connection.close()

    def __init__(self):
        config = self.load_config()
        self.connection = None
        try:    
            self.connection = self.connect(config)
            self.cursor = self.connection.cursor()
        except (psycopg2.Error) as error:
            print("There was an error with postgresql.", error)
            self.close()
            sys.exit()
    
    def __del__(self):
        self.close()
    
    def add_word(self, word: str):
        print(word)
        # vulnerable to injection exploits
        try:
            self.cursor.execute("INSERT INTO words (word) VALUES (%s)", (word,))
        except Exception as sqlException:
            print("There was an exception from postgres!", sqlException)
