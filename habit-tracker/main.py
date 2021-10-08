import requests

pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = "ygud5u6uihloicxrw5ty6tgo8ho"

user_params = {
    "token": pixela_token,
    "username": "glo-stick",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
