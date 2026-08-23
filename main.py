from flask import Flask, request, jsonify
from google.cloud import geminidataanalytics_v1alpha1 as gda
import os

app = Flask(__name__)

client = gda.DataAnalyticsClient()
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "tu-proyecto-id")
LOCATION = "us-central1"
AGENT_ID = "analista-arboles-sf"

@app.route("/", methods=["POST"])
def ask_agent():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "El campo 'prompt' es obligatorio."}), 400
        prompt = data["prompt"]
        agent_path = f"projects/{PROJECT_ID}/locations/{LOCATION}/agents/{AGENT_ID}"
        response = client.query_agent(name=agent_path, query=prompt)
        return jsonify({"response": response.result, "status": "success"})
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)