from os import environ
import psycopg2


class Database:
    def connect():
        return psycopg2.connect(
            dbname=environ.get("DB_NAME"),
            host=environ.get("DB_HOST"),
            password=environ.get("DB_PASS"),
            user=environ.get("DB_USER"),
        )

    @classmethod
    def get_users_from_db(self):
        cursor = self.connect().cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()
        cursor.close()
        return users

    @classmethod
    def get_user_from_db_by_id(self, id):
        cursor = self.connect().cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s;", [id])
        user = cursor.fetchone()
        cursor.close()
        return user

    @classmethod
    def create(self, data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, cpf) VALUES (%s, %s) RETURNING *",
            (data["name"], data["cpf"]),
        )
        conn.commit()
        user = cursor.fetchone()
        cursor.close()
        return user
