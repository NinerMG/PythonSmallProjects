import requests


# ?amount=10&category=11&type=boolean"

parameters = {
    "amount": 10,
    "category": 11,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]

