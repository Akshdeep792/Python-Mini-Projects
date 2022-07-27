
from urllib import response
import requests
from datetime import *
pixela_endpoint = "https://pixe.la/v1/users"


USERNAME = "post-test"
TOKEN = "amb2aes1bae7na"
parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

# response = requests.post(pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph217",
    "name": "Exercise Graph",
    "unit": "min",
    "type" : "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

graph_id = graph_parameters["id"]
pixel_endpoint = f"{graph_endpoint}/{graph_id}"


today_date = datetime.now()
pixel_parameters = {
    "date" : today_date.strftime("%Y%m%d"),
    "quantity" :  input("How many minutes did you workout today? ")
}

response = requests.post(url = pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)


#***********Delete Pixel
# date_to_delete = today_date.strftime("%Y%m%d")
# delete_endpoint = f"{pixel_endpoint}/{date_to_delete}"

# response = requests.delete(url = delete_endpoint, headers=headers)
# print(response.text)

