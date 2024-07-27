from infra.service.pg_service import PgService


class UserService(PgService):
    @classmethod
    def get_all_from_db(self):
        return self.run_query(
            query="SELECT * FROM users ORDER BY created_at DESC", parameters=[]
        )

    @classmethod
    def get_from_db_by_id(self, id):
        return self.run_query("SELECT * FROM users WHERE id = %s;", [id])

    @classmethod
    def get_from_db_by_cpf(self, cpf):
        return self.run_query("SELECT * FROM users WHERE cpf = %s;", [cpf])

    @classmethod
    def create(self, data):
        response = self.run_query(
            "INSERT INTO users (name, cpf, email) VALUES (%s, %s, %s) RETURNING *",
            (data["name"], data["cpf"], data["email"]),
        )
        return response[0]

    @classmethod
    def update(self, id, data):
        response = self.run_query(
            "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING *",
            (data["name"], data["email"], id),
        )
        return response[0]

    @classmethod
    def delete(self, id):
        response = self.run_query(
            "DELETE FROM users WHERE id = %s RETURNING *",
            (id),
        )
        return response[0]
