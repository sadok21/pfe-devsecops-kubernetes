from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "PFE DevSecOps Kubernetes",
        "message": "Application Flask déployée avec succès",
        "status": "running",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/info")
def info():
    return jsonify({
        "author": "Sadok Bouzrati",
        "project_type": "Engineering PFE",
        "stack": [
            "Python Flask",
            "Docker",
            "Kubernetes K3s",
            "GitHub Actions",
            "SonarQube",
            "Trivy",
            "Prometheus",
            "Grafana"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
