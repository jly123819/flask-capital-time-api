# Flask API for City Time with Token Authentication

## Overview
This Flask API provides an endpoint to retrieve the current local time and UTC offset for a given capital city. It requires token-based authentication to access the protected endpoint. The API is hosted on a GCP instance and is accessible via a public IP.

## API Details

### Base URL
```
http://34.45.208.227:5002
```

### Endpoints

#### 1. Get City Time
- **Endpoint**: `/api/time/<city>`
- **Method**: `GET`
- **Description**: Returns the current local time and UTC offset for the specified capital city in JSON format.
- **Parameters**:
  - `city` (path parameter): The name of the capital city (e.g., `Tokyo`, `London`). Case-insensitive.
- **Headers**:
  - `Authorization`: Bearer token (required). Use `Bearer supersecrettoken123`.
- **Success Response** (200):
  ```json
  {
    "city": "Tokyo",
    "local_time": "2025-04-20 20:34:56",
    "utc_offset": "UTC+9.0"
  }
  ```
- **Error Responses**:
  - **401 Unauthorized** (if token is missing or invalid):
    ```json
    {"error": "Unauthorized"}
    ```
  - **404 Not Found** (if city is not in the database):
    ```json
    {"error": "City 'Paris' not found in database"}
    ```

#### 2. Hello (Open Endpoint)
- **Endpoint**: `/api/hello`
- **Method**: `GET`
- **Description**: A simple endpoint to test if the API is running.
- **Headers**: None required.
- **Success Response** (200):
  ```json
  {"message": "Hello, world!"}
  ```

#### 3. Secure Data (Protected Endpoint)
- **Endpoint**: `/api/secure-data`
- **Method**: `GET`
- **Description**: A protected endpoint to test token authentication.
- **Headers**:
  - `Authorization`: Bearer token (required). Use `Bearer supersecrettoken123`.
- **Success Response** (200):
  ```json
  {"secret": "This is protected info!"}
  ```
- **Error Response** (401):
  ```json
  {"error": "Unauthorized"}
  ```

## How to Call the API

### Using `curl`
1. **Get city time (e.g., Tokyo)**:
   ```bash
   curl -H "Authorization: Bearer supersecrettoken123" http://34.45.208.227:5002/api/time/Tokyo
   ```
   **Expected Output**:
   ```json
   {"city": "Tokyo", "local_time": "2025-04-20 20:34:56", "utc_offset": "UTC+9.0"}
   ```

2. **Test unauthorized access**:
   ```bash
   curl http://34.45.208.227:5002/api/time/Tokyo
   ```
   **Expected Output**:
   ```json
   {"error": "Unauthorized"}
   ```

3. **Test invalid city**:
   ```bash
   curl -H "Authorization: Bearer supersecrettoken123" http://34.45.208.227:5002/api/time/Paris
   ```
   **Expected Output**:
   ```json
   {"error": "City 'Paris' not found in database"}
   ```

### Using Python (`requests` library)
You can use the following Python script to call the API:
```python
import requests

API_URL = "http://34.45.208.227:5002/api/time/Tokyo"
TOKEN = "supersecrettoken123"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
```
**Expected Output**:
```
Success: {'city': 'Tokyo', 'local_time': '2025-04-20 20:34:56', 'utc_offset': 'UTC+9.0'}
```

## Supported Cities
The API supports the following capital cities:
- Washington (`America/New_York`)
- London (`Europe/London`)
- Tokyo (`Asia/Tokyo`)
- Canberra (`Australia/Canberra`)
- Beijing (`Asia/Shanghai`)

## Notes
- Ensure the `Authorization` header is included with the correct token (`supersecrettoken123`).
- The API is case-insensitive for city names (e.g., `Tokyo`, `tokyo`, `TOKYO` are all valid).
- The API is hosted on a GCP instance, and the IP address may change if the instance is restarted. Check the latest IP in the GCP Console.
