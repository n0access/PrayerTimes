from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/prayer_times.yaml")
def serve_yaml():
    return send_from_directory(directory=os.getcwd(), path="prayer_times.yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
