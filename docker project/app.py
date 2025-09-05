import psycopg2
import time

time.sleep(5)  # wait for Postgres to start

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("Connected to the database!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)


