from infra.service.user_service import UserService
from infra.model.user_model import User
from utils.custom_exception import CustomException
import re


class CreateUser:

    @classmethod
    def execute(self, data):
        data["cpf"] = re.sub("[^0-9]", "", data["cpf"])
        if not len(data["cpf"]) == 11:
            raise CustomException("Invalid cpf", 401)
        user_already_exists = UserService.get_from_db_by_cpf(data["cpf"])
        if user_already_exists:
            raise CustomException("User already exists", 409)
        new_user_from_db = UserService.create(data)
        return User(new_user_from_db).to_dict()
