from os import environ
import psycopg2


class Database:
    def connect():
        conn = psycopg2.connect(
            dbname=environ.get("DB_NAME"),
            host=environ.get("DB_HOST"),
            password=environ.get("DB_PASS"),
            user=environ.get("DB_USER"),
        )
        return conn.cursor()

    @classmethod
    def get_users_from_db(self):
        cursor = self.connect()
        cursor.execute("select * from users limit 1")
        users = cursor.fetchmany()
        cursor.close()
        return users

    @classmethod
    def get_user_from_db_by_id(self, id):
        cursor = self.connect()
        cursor.execute("select * from users where id = %s", (id))
        user = cursor.fetchone()
        cursor.close()
        return user
