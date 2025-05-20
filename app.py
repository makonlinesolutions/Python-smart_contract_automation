from flask import Flask, request, jsonify
from automation.run_master import run_master
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/api/start", methods=["POST"])
def start():
    with open("payloads/last-run.json", "w") as f:
        json.dump(request.json, f)
    
    run_master()
    return jsonify({ "message": "✅ Automation started" })

if __name__ == "__main__":
    app.run(port=3000)