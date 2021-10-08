import os
import datetime
import requests

USERNAME = "omoh-ship"

# CREATE USER
pixela_token = os.environ['PIXELA_TOKEN']
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": "omoh-ship",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "hrs",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": pixela_token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# CREATE PIXEL POINT
pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.datetime(year=2021, month=10, day=4)

pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "3",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# UPDATE PIXEL
update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": "10",
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# DELETE PIXEL
delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
