import os
from os.path import join, dirname
from dotenv import load_dotenv
import mysql.connector

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST") or "localhost",
            port=os.environ.get("DB_POST") or 3306,
            user=os.environ.get("DB_USER") or "root",
            password=os.environ.get("DB_PASSWORD") or "root",
            database=os.environ.get("DB_DATABASE") or "nettruyen_db",
        )

        # if conn:
        #     print("Successfully connected to the database.")

        return conn
    except Exception as e:
        print("Error connecting to the database: ", e)
        return None
