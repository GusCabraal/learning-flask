from infra.service.pg_service import PgService


class UserService(PgService):
    @classmethod
    def get_all_from_db(self):
        return self.run_query(
            query="SELECT * FROM users ORDER BY created_at DESC", parameters=[]
        )

    @classmethod
    def get_from_db_by_id(self, id):
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
    
    @classmethod
    def delete(self, id):
        response = self.run_query(
            "DELETE FROM users WHERE id = %s RETURNING *",
            (id),
        )
        return response[0]
