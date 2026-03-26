from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the calculator API!", 200


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


def get_numbers():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    return a, b


@app.route("/add", methods=["POST"])
def add():
    a, b = get_numbers()
    return jsonify({"result": a + b}), 200


@app.route("/subtract", methods=["POST"])
def subtract():
    a, b = get_numbers()
    return jsonify({"result": a - b}), 200


@app.route("/multiply", methods=["POST"])
def multiply():
    a, b = get_numbers()
    return jsonify({"result": a * b}), 200


@app.route("/divide", methods=["POST"])
def divide():
    a, b = get_numbers()
    if b == 0:
        return jsonify({"error": "Division by zero"}), 400
    return jsonify({"result": a / b}), 200


if __name__ == "__main__":
    app.run(debug=True)
