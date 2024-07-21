from flask import Flask, jsonify, request
from infra.db import Database
from infra.model.user_model import User


app = Flask(__name__)


@app.route("/")
def get_users():
    users_from_db = Database.get_users_from_db()
    users = [User(user).to_dict() for user in users_from_db]
    return jsonify(users)


@app.route("/<id>")
def get_user_by_id(id):
    user_from_db = Database.get_user_from_db_by_id(id)
    user = User(user_from_db).to_dict()
    return jsonify(user)


@app.route("/", methods=["POST"])
def create_user():
    new_user_from_db = Database.create(request.json)
    new_user = User(new_user_from_db).to_dict()
    return jsonify(new_user)


def start_server(host: str = "0.0.0.0", port: int = 8000):
    print(f"Server in running on port {port}")
    return app.run(debug=True, host=host, port=port)


if __name__ == "__main__":
    start_server()
