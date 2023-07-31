from flask import Flask, request
from flask_cors import CORS
from src.poetry_chain import poetry_chain

app = Flask(__name__)
CORS(app)

@app.route("/poetry", methods=["POST"])
def poetry():
    body = request.get_json()
    if not body.get("messages"):
        return { "status_code": 400, "error": "field \"messages\" must be required" }, 400
    return poetry_chain(body["messages"]), { "Content-Type": "text/plain" }