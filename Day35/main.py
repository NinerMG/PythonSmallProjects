import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "74b817341b0a7e303863fee12cda57a0"

weather_params = {
    "lat": 50.064651,
    "lon": 19.944981,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
    #    print("Bring an umbrella.")
        will_rain = True

if will_rain:
    print("Bring an umbrella")

