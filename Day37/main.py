import requests
from datetime import datetime


# sprawdzać w dokumentacji witryny
# https://pixe.la/v1/users/niner4/graphs/graph1.html

USERNAME = "niner4"
TOKEN = "hjkh32h321dsadas31"
pixela_endpoint = "https://pixe.la/v1/users"
my_user_endpoint = "https://pixe.la/@niner4"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# utworzono usera, można już zakomentować
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.json())

# create graph
# graph_endpoint = "https://pixe.la/v1/users/a-know/graphs"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# do stworzenenia grafu
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.json())

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
"quantity": "1.24",
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.json())

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.json())