import psycopg2
from config import *
conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
print(conn)
conn.autocommit = True
cursor = conn.cursor()
with conn.cursor() as cursor:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS phonebook(
            Name text PRIMARY KEY,
            number text NOT NULL);"""
    )

cursor.close()
conn.close()