import requests

response =requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

data = response.json()["iss_position"]
print(data)