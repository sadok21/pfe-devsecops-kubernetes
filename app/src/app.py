from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "project": "PFE DevSecOps Kubernetes",
        "message": "Application Flask deployee",
        "status": "running",
        "version": "1.0.0"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.get("/info")
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