import requests

SHEETY_ENDPOINT = "https://api.sheety.co/6bbf5e5da8baa33e97bf83894678fb1d/mgFlight/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

