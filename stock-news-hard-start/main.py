import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = os.environ['STOCK_API_KEY']
news_api_key = os.environ['NEWS_API_KEY']
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

FIVE_PERCENT = 0.05
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
#interval=5min
news_params = {
    "qInTitle": COMPANY_NAME,
    "from": "2021-09-29",
    "to": "2021-09-30",
    "sortBy": "popularity",
    "pageSize": 3,
    "apiKey": news_api_key,
}


# STEP 1: Use https://newsapi.org/docs/endpoints/everything
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value["4. close"] for (key, value) in stock_data.items()]
yesterday_stock_price = float(data_list[0])
day_before_yes_stock_price = float(data_list[1])

positive_diff = yesterday_stock_price - day_before_yes_stock_price
up_down = None
if positive_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference_percentage = round(positive_diff / yesterday_stock_price * 100)

if abs(positive_diff) > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    # article = [article["content"] for article in articles]
    send = [Client(account_sid, auth_token).messages.create(
            body=f"{STOCK}: {up_down}{difference_percentage}% change\nHeadline: {article['title']}\nBrief: {article['description']}\n",
            from_="+12178852612",
            to="+2348080174320"
            ) for article in articles]
