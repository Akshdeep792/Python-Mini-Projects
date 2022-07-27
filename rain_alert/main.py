
from sqlite3 import paramstyle
import requests
from twilio.rest import Client

account_sid = "your api_id"
auth_token = "auth_token"
api_key = "Your API Key"

parameters = {
    "lat" : 26.238947,
    "lon" : 73.024307,
    "appid" : api_key,
    "exclude" : "currently,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters) #open weather
response.raise_for_status() 

data = response.json()
hourly_list = data["hourly"][:12]


will_rain = False
for hour_data in hourly_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
# print(hourly_list)s


if will_rain:
    client = Client(account_sid, auth_token) #twilio

    message = client.messages \
                    .create(
                        body="It's going to rain today",
                        from_='+17372327033',
                        to='+918396927527'
                    )
    print(message.status)