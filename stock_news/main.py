STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "YOUR_API"

NEWS_API_KEY ="YOUR_APi"
from numpy import diff, floor
import requests

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={API_KEY}")
data = response.json()

market_time = data["Time Series (60min)"]

iterator = 0
diff_list = []
for date_time in market_time:
    if iterator == 0 or iterator == 16:
        diff_list.append(market_time[date_time])
    iterator +=1



diff_stocks = float(diff_list[0]["4. close"]) - float(diff_list[1]["4. close"])

percentage_stock = (diff_stocks/float(diff_list[0]["4. close"]))*100

if abs(percentage_stock) < 5:
    
    response_2 = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2022-07-27&sortBy=popularity&apiKey={NEWS_API_KEY}")
    data_2 = response_2.json()
    
    news_list = data_2["articles"][:3]
    
 

    sample_list = []
    for news in news_list:

        temp_dict = {
            "Title": news["title"],
            "Brief" : news["description"]
        }
        sample_list.append(temp_dict)
    if percentage_stock < 0:
        print(f"🔻 {abs(percentage_stock)}")
    else:
        print(f"🔺 {abs(percentage_stock)}")

    print(sample_list)


