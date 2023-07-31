from flask import Flask, request
from flask_cors import CORS
from src.poetry_chain import poetry_chain
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/poetry", methods=["POST"])
def poetry():
    print("bateu aqui")
    body = request.get_json()
    if not body.get("messages"):
        return {"status_code": 400, "error": "field \"messages\" must be required"}, 400
    return poetry_chain(body["messages"]), {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(debug=False, threaded=True)
