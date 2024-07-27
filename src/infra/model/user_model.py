class User:
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.email = data[2]
        self.created_at = data[3]
        self.cpf = data[4]

    def to_dict(self):
        return {"id": self.id, "name": self.name, "cpf": self.cpf, "email": self.email}
