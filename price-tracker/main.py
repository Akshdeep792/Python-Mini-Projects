from bs4 import BeautifulSoup
from click import prompt
from twilio.rest import Client

import requests


your_price = 50000

account_sid = "Twilio Sid"
auth_token = "Your Token"
url = "https://www.amazon.in/Apple-iPad-Air-10-9-inch-27-69-Wi-Fi/dp/B09V4FNFHN/ref=sr_1_3?crid=25X56W2PZMDGA&keywords=ipad&qid=1659153197&sprefix=ipad%2Caps%2C317&sr=8-3&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=url, headers=header)
product_page = response.text

soup = BeautifulSoup(product_page, "html.parser")

price = soup.find(class_="a-price-whole")
prod_price = price.get_text().split(".")[0].split(",")

prod_price = prod_price[0] + prod_price[1]
print(prod_price)

if int(prod_price) < your_price:
    client = Client(account_sid, auth_token) #twilio

    message = client.messages \
                    .create(
                        body=f"You can buy the following Product. {url}",
                        from_='+17372327033',
                        to='+918396927527'
                    )
    print(message.status)