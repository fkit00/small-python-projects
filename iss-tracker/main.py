import requests
from datetime import datetime
import time 

MY_LAT = 51.507351
MY_LONG =  -0.127758

def is_iss_overhead():
    response =requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()["iss_position"]

    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])

    if MY_LAT -5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    params ={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    data=response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        #it's dark 
        return True 


# this gives us the hours of the sunrise times - now we want to test wether it's close to our position
#our margin is + or - 5
# we want to compare our lat and long with the iss and add in a degree of error
# 
while True: 
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look up!")
    else:
        print("nothing to see here")