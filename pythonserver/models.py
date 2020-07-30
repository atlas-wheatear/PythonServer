from dotenv import load_dotenv
import psycopg2
import sys
import os

class Model():    
    def connect(self):
        connection = psycopg2.connect(
            user = os.getenv("POSTGRES_USER"),
            host = os.getenv("POSTGRES_HOSTNAME"),
            port = 5432,
            dbname = os.getenv("POSTGRES_DB"),
            password = os.getenv("POSTGRES_PASSWORD")
        )
        return connection
    
    def close(self):
        if (self.connection):
            self.cursor.close()
            self.connection.close()

    def __init__(self):
        load_dotenv()
        self.connection = None
        try:    
            self.connection = self.connect()
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
