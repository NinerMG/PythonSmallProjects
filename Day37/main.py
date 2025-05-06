import requests

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

graph_config = {
    "id": "graph1",
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

pixel_creation_endpoint
