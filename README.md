Flask API for City Time with Token Authentication
Overview
This Flask API provides an endpoint to retrieve the current local time and UTC offset for a given capital city. It requires token-based authentication to access the protected endpoint. The API is hosted on a GCP instance and is accessible via a public IP.
API Details
Base URL
http://34.45.208.227:5002
Endpoints
1. Get City Time
Endpoint: /api/time/<city> 
Method: GET 
Description: Returns the current local time and UTC offset for the specified capital city in JSON format. 
Parameters:city (path parameter): The name of the capital city (e.g., Tokyo, London). Case-insensitive. 
Headers:Authorization: Bearer token (required). Use Bearer supersecrettoken123. 
Success Response (200):{
  "city": "Tokyo",
  "local_time": "2025-04-20 20:34:56",
  "utc_offset": "UTC+9.0"
}
Error Responses:401 Unauthorized (if token is missing or invalid):{"error": "Unauthorized"}
404 Not Found (if city is not in the database):{"error": "City 'Paris' not found in database"}
2. Hello (Open Endpoint)
Endpoint: /api/hello 
Method: GET 
Description: A simple endpoint to test if the API is running. 
Headers: None required. 
Success Response (200):{"message": "Hello, world!"}
3. Secure Data (Protected Endpoint)
Endpoint: /api/secure-data 
Method: GET 
Description: A protected endpoint to test token authentication. 
Headers:Authorization: Bearer token (required). Use Bearer supersecrettoken123. 
Success Response (200):{"secret": "This is protected info!"}
Error Response (401):{"error": "Unauthorized"}
How to Call the API
Using curl
Get city time (e.g., Tokyo):
curl -H "Authorization: Bearer supersecrettoken123" http://34.45.208.227:5002/api/time/Tokyo
Expected Output:
{"city": "Tokyo", "local_time": "2025-04-20 20:34:56", "utc_offset": "UTC+9.0"}
Test unauthorized access:
curl http://34.45.208.227:5002/api/time/Tokyo
Expected Output:
{"error": "Unauthorized"}
Test invalid city:
curl -H "Authorization: Bearer supersecrettoken123" http://34.45.208.227:5002/api/time/Paris
Expected Ou
