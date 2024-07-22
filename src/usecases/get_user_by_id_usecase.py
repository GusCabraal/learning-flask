from infra.service.user_service import UserService
from infra.model.user_model import User
from utils.custom_exception import CustomException


class GetUserById:

    @classmethod
    def execute(self, id):
        user_from_db = UserService.get_from_db_by_id(id)
        if len(user_from_db) == 0:
            raise CustomException("User not found", 404)
        user = User(user_from_db[0]).to_dict()
        return user
