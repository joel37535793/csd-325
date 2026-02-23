import requests
import json

response = requests.get("http://api.open-notify.org/astros")
print("Status Code:", response.status_code)

data = response.json()

print("\nNumber of astronauts in space:", data["number"])
print("\nAstronauts currently in space:")

for person in data["people"]:
    print(person["name"], "-", person["craft"])
