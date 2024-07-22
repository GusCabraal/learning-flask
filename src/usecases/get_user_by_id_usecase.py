from infra.service.user_service import UserService
from infra.model.user_model import User


class GetUserById:

    @classmethod
    def execute(self, id):
        user_from_db = UserService.get_from_db_by_id(id)
        if len(user_from_db) == 0:
            raise Exception("User not found")
        user = User(user_from_db[0]).to_dict()
        return user
