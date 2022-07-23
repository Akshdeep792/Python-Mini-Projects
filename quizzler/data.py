import requests

parameters = {
    "amount" : 10,
    "category": 18,
    "type":"boolean"

}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
# print(data["results"])

question_data = data["results"]