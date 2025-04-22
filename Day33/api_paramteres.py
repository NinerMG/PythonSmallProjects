import requests
import datetime

MY_LAT = 50.061500
MY_LONG = 19.937999

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0

}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.datetime.now().hour
print(time_now)