import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env/.env"))

class PostgresHandler ():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def initialize_conn(self):
        try:
            conn = psycopg2.connect(host=os.getenv("DB_LOC"), dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"))
            cur = conn.cursor()
            print('Connection established')
            self.connection, self.cursor = conn, cur
            return conn, cur
        except Exception as e:
            print(f"An error ocurred the conneciton could not be established.\nError: {e}")

    def get_price_data_gas(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
