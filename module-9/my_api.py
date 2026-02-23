import requests
import json

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

# Test connection
print("Status Code:", response.status_code)

# Print raw response
print("\nRaw Response:")
print(response.json())

# Print formatted output
data = response.json()

print("\nFormatted Joke:")
print("Setup:", data["setup"])
print("Punchline:", data["punchline"])