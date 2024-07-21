from os import environ
import psycopg2


class PgService:
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
