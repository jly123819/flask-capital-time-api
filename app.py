from flask import Flask, jsonify, request
from functools import wraps
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

capital_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Washington": "America/New_York",
    "Beijing": "Asia/Shanghai"
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer ") or auth.split(" ")[1] != API_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/capital-time', methods=['GET'])
@token_required
def capital_time():
    city = request.args.get('city')
    print(f"Received request for city: {city}")  # Debug line
    if not city or city not in capital_timezones:
        return jsonify({"error": "City not found"}), 404

    tz = pytz.timezone(capital_timezones[city])
    local_time = datetime.now(tz)
    utc_offset = local_time.strftime('%z')
    return jsonify({
        "city": city,
        "local_time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": f"{utc_offset[:3]}:{utc_offset[3:]}"
    })

@app.route('/')
def index():
    return 'Welcome! Use /api/capital-time?city=YourCapital with Bearer token.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
