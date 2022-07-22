
import requests

MY_LAT = 30.378180
MY_LONG = 76.7766954

parameters = {
    "lat" : MY_LAT,
    "long" : MY_LONG
}

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()


# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# co_ordinates = (longitude, latitude)
# print(co_ordinates)

# response = requests.get(url="https://api.kanye.rest/")
# response.raise_for_status()
# data = response.json()

# quote = data["quote"]
# print(f"Quote: {quote}")

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)