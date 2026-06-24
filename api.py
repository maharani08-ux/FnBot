from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/music")
def get_music():
    with open("music.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)