from flask import Flask, jsonify
from presentation.controller.users_controller import users_controller


app = Flask(__name__)

app.register_blueprint(users_controller, url_prefix="/users")


@app.errorhandler(Exception)
def handle_default_exception(error):
    return jsonify({"message": error.args[0]})


def start_server(host: str = "0.0.0.0", port: int = 8000):
    print(f"Server in running on port {port}")
    return app.run(debug=True, host=host, port=port)


if __name__ == "__main__":
    start_server()
