import requests

MY_LAT = 51.507351
MY_LONG =  -0.127758

# response =requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# data = response.json()["iss_position"]
# print(data)

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

# iss_positon=(longitude, latitude)
# print(iss_positon)


params ={
    "lat":MY_LAT,
    "lng":MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
data=response.json()
print(data)
