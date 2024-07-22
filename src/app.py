from flask import Flask, jsonify
from presentation.controller.users_controller import users_controller
from utils.custom_exception import CustomException


app = Flask(__name__)

app.register_blueprint(users_controller, url_prefix="/users")


@app.errorhandler(CustomException)
def handle_custom_exception(error):
    return jsonify({"message": error.message}), error.status_code


def start_server(host: str = "0.0.0.0", port: int = 8000):
    print(f"Server in running on port {port}")
    return app.run(debug=True, host=host, port=port)


if __name__ == "__main__":
    start_server()
