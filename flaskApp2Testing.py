import requests

BASE_URL = "http://127.0.0.1:5000"

print(requests.get(f"{BASE_URL}/hello").json())
print(requests.get(f"{BASE_URL}/data").json())

new_item = {
    "campus": "Test Campus",
    "lat": 0.0,
    "lon": 0.0
}

print(requests.post(f"{BASE_URL}/data", json=new_item).json())