from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/random-wikipedia-link", methods=["GET"])
def get_random_wikipedia_link():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    return jsonify({"url": response.url})


if __name__ == "__main__":
    app.run(debug=True)
