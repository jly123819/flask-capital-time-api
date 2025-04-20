from flask import Flask, jsonify, request
from datetime import datetime
import pytz
from functools import wraps

app = Flask(__name__)
API_TOKEN = "supersecrettoken123"  # In production, use environment variables

# Dictionary of capital cities and their time zones
CAPITAL_CITIES = {
    "washington": "America/New_York",
    "london": "Europe/London",
    "tokyo": "Asia/Tokyo",
    "canberra": "Australia/Canberra",
    "beijing": "Asia/Shanghai"
}


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401

    return decorator


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})


@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})


@app.route('/api/time/<city>', methods=['GET'])
@token_required
def get_city_time(city):
    city = city.lower()
    if city not in CAPITAL_CITIES:
        return jsonify({"error": f"City '{city}' not found in database"}), 404

    timezone = pytz.timezone(CAPITAL_CITIES[city])
    local_time = datetime.now(timezone)

    # Calculate UTC offset
    utc_offset = local_time.utcoffset()
    if utc_offset is not None:
        utc_offset_hours = utc_offset.total_seconds() / 3600
        offset_str = f"UTC{'+' if utc_offset_hours >= 0 else ''}{utc_offset_hours:.1f}"
    else:
        offset_str = "UTC+0.0"

    return jsonify({
        "city": city.capitalize(),
        "local_time": local_time.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": offset_str
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
    
