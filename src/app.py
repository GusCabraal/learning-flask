from flask import Flask, jsonify
from infra.db import get_users_from_db
from infra.model.user_model import User


app = Flask(__name__)


@app.route("/")
def get_users():
    users_from_db = get_users_from_db()
    users = [User(user).to_dict() for user in users_from_db]
    return jsonify(users)


def start_server(host: str = "0.0.0.0", port: int = 8000):
    print(f"Server in running on port {port}")
    return app.run(debug=True, host=host, port=port)


if __name__ == "__main__":
    start_server()
