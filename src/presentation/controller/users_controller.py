from flask import jsonify, request, Blueprint
from infra.service.user_service import UserService
from usecases.get_user_by_id_usecase import GetUserById
from usecases.create_user_usecase import CreateUser
from infra.model.user_model import User

users_controller = Blueprint("users", __name__)


@users_controller.route("/")
def get_users():
    users_from_db = UserService.get_all_from_db()
    users = [User(user).to_dict() for user in users_from_db]
    return jsonify(users)


@users_controller.route("/<id>")
def get_user_by_id(id):
    user = GetUserById.execute(id)
    return jsonify(user)


@users_controller.route("/", methods=["POST"])
def create_user():
    new_user = CreateUser.execute(request.json)
    return jsonify(new_user)


@users_controller.route("/<id>", methods=["PUT"])
def update_user_by_id(id):
    updated_user_from_db = UserService.update(id, request.json)
    updated_user = User(updated_user_from_db).to_dict()
    return jsonify(updated_user)


@users_controller.route("/<id>", methods=["DELETE"])
def delete_user_by_id(id):
    deleted_user_from_db = UserService.delete(id)
    deleted_user = User(deleted_user_from_db).to_dict()
    return jsonify(deleted_user)
