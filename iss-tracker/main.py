import requests
from datetime import datetime

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
    "lng":MY_LONG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
data=response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now=datetime.now()
print(time_now)
print(sunrise.split("T")[1].split(":")[0],sunset.split("T")[1].split(":")[0])
print(time_now.hour)
# this gives us the hours of the sunrise times