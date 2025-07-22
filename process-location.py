from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process-location', methods=['POST'])
def process_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    user_agent = data.get('userAgent')
    ip_address = request.remote_addr

    print(f"\n📍 Location Pinged at {datetime.datetime.now()}", flush=True)
    print(f"Latitude: {latitude}", flush=True)
    print(f"Longitude: {longitude}", flush=True)
    print(f"IP Address: {ip_address}", flush=True)
    print(f"User Agent: {user_agent}", flush=True)
    print("--------------------------------------------------", flush=True)

    return jsonify({"status": "success", "ip": ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
