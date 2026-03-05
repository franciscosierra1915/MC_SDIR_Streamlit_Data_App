import requests

URL = "http://localhost:5000/api/items"

response = requests.get(URL).json()

print(response)