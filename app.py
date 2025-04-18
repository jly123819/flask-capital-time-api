from flask import Flask, jsonify, request

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

# Handles the homepage
@app.route('/')
def index():
    return 'Welcome! Try /api/hello or /api/secure-data'

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)


