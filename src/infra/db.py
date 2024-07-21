from os import environ
import psycopg2


def get_users_from_db():
    try:
        conn = psycopg2.connect(
            dbname=environ.get("DB_NAME"),
            host=environ.get("DB_HOST"),
            password=environ.get("DB_PASS"),
            user=environ.get("DB_USER"),
        )
        cursor = conn.cursor()
        cursor.execute("select * from users limit 1")
        users = cursor.fetchmany()
        return users
    except psycopg2.Error as e:
        print(e)
        return e
