from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

counter = {
    "count":0
}

@app.route("/count", methods=["GET"])
def get_count():
    return jsonify(counter)

@app.route("./increment", methods=["POST"])
def increment():
    counter["count"] += 1
    return jsonify(counter)

@app.route("/decrement", methods=["POST"])
def decrement():
    counter["count"] -= 1
    return jsonify(counter)

if __name__ == "__main__":
    app.run(debug=True)

