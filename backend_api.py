from flask import Flask, request, jsonify
import json
import os
from automation.run_master import run_master

app = Flask(__name__)

@app.route("/api/start", methods=["POST"])
def start_automation():
    try:
        data = request.get_json()
        payload_path = os.path.join(os.path.dirname(__file__), 'payloads', 'last-run.json')
        with open(payload_path, 'w') as f:
            json.dump(data, f, indent=2)

        # Run automation AFTER saving file
        run_master()

        return jsonify({"message": "✅ Automation complete!"})
    except Exception as e:
        print("❌ Backend error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000)
