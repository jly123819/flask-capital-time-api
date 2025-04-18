# Flask Capital Time API
Initial file to enable branch.
---

# Flask Capital Time API

A simple Flask API hosted on GCP that returns the current time and UTC offset of a given capital city. Only authorized users with a valid token can access the endpoint.

---

## 🔐 Token Authentication

All API requests must include a Bearer token in the header:

# Authorization: Bearer supersecrettoken123


---

## 🌐 API Usage

### Endpoint:
`GET /api/capital-time?city=London`

Returns the current time and UTC offset for the given capital city.

---

### ✅ Example (Success)

**Request:**
```bash
curl -H "Authorization: Bearer supersecrettoken123" "http://<YOUR-IP>:5002/api/capital-time?city=London"


# Response:
{
  "city": "London",
  "local_time": "2025-04-18 19:45:00",
  "utc_offset": "+01:00"
}

# ❌ Example (City not found)
# Request:
curl -H "Authorization: Bearer supersecrettoken123" "http://<YOUR-IP>:5002/api/capital-time?city=Hogwarts"

# Response:
{
  "error": "City not found"
}

# ❌ Example (Missing or invalid token)
{
  "error": "Unauthorized"
}


---
