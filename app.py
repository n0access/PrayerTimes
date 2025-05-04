from flask import Flask, send_from_directory
import os
import subprocess
subprocess.run(["python", "scrape_prayer_times.py"], check=True)
app = Flask(__name__)

@app.route('/prayer_times.json')
def serve_json():
    return send_from_directory(directory=os.getcwd(), path='prayer_times.json', mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)