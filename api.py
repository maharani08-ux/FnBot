from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

JSONBIN_ID = os.getenv("JSONBIN_ID")
JSONBIN_KEY = os.getenv("JSONBIN_KEY")

@app.route("/music")
def get_music():
    url = f"https://api.jsonbin.io/v3/b/{JSONBIN_ID}/latest"
    headers = {
        "X-Master-Key": JSONBIN_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify(data.get("record", data))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)