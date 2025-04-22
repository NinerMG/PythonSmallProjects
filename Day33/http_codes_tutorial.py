# status code responses
# https://www.webfx.com/web-development/glossary/http-status-codes/

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# if response.status_code == 404:
#     raise Exception("That resource does not exists")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data")

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

#print(data)
#print(longitude)
#print(latitude)

print(iss_position)