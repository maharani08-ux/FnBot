from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/music")
def get_music():
    with open("music.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)