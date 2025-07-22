from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin from ngrok

@app.route('/process-location', methods=['POST'])
def process_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    user_agent = data.get('userAgent')
    ip_address = request.remote_addr

    print(f"\n📍 Location Pinged at {datetime.datetime.now()}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"IP Address: {ip_address}")
    print(f"User Agent: {user_agent}")
    print("--------------------------------------------------")

    return jsonify({"status": "success", "ip": ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
