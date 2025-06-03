import requests

# Test GET
r_get = requests.get("http://localhost:5000/generate", params={"keyword": "wireless earbuds"})
print("GET Response:", r_get.json())

# Test POST
r_post = requests.post("http://localhost:5000/generate", json={"keyword": "wireless earbuds"})
print("POST Response:", r_post.json())

