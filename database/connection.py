import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST") or "localhost",
            port=os.getenv("DB_POST") or 3309,
            user=os.getenv("DB_USER") or "root",
            password=os.getenv("DB_PASSWORD") or "123456",
            database=os.getenv("DB_DATABASE") or "db_nettruyen",
        )

        if conn:
            print("Successfully connected to the database.")

        return conn
    except Exception as e:
        print("Error connecting to the database: ", e)
        return None
