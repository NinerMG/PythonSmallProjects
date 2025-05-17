import requests
from requests.auth import HTTPBasicAuth

SHEETY_ENDPOINT = "https://api.sheety.co/6bbf5e5da8baa33e97bf83894678fb1d/mgFlight/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = "test"
        self.password = "test"
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)