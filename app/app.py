from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    logging.info("Root endpoint accessed")
    return "Hello from Docker on AWS using DevOps 🚀"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
