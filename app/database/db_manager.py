import sqlite3
from  EnvConfig import app_settings

class DBManager:
    def __init__(self):
        config = EnvConfig()
        self.db_name = config.DB_NAME
        self.connection = None
        self.cursor = None
        self.create_connection()


    def create_connection(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to SQLite database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
