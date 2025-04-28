import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")
account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="+16204592963",
        to=os.environ.get("OWN_REC_NUMBER"),
    )
    print(message.status)