from os import environ
import psycopg2


class Database:
    @classmethod
    def get_users_from_db(self):
        return self.run_query("SELECT * FROM users ORDER BY created_at DESC", [])

    @classmethod
    def get_user_from_db_by_id(self, id):
        response = self.run_query("SELECT * FROM users WHERE id = %s;", [id])
        return response[0]

    @classmethod
    def create(self, data):
        response = self.run_query(
            "INSERT INTO users (name, cpf) VALUES (%s, %s) RETURNING *",
            (data["name"], data["cpf"]),
        )
        return response[0]

    @classmethod
    def update(self, id, data):
        response = self.run_query(
            "UPDATE users SET name = %s, cpf = %s WHERE id = %s RETURNING *",
            (data["name"], data["cpf"], id),
        )
        return response[0]

    def run_query(query, parameters):
        try:
            connection = psycopg2.connect(
                dbname=environ.get("DB_NAME"),
                host=environ.get("DB_HOST"),
                password=environ.get("DB_PASS"),
                user=environ.get("DB_USER"),
            )
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Faiure running query", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
