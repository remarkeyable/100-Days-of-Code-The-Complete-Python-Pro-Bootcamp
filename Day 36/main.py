import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "http://api.marketstack.com/v1/eod"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = ""
API_KEY2 = ""


parameter = {
    "apiKey": API_KEY,
    "q": COMPANY_NAME,
}

params_stock = {
    "symbols":STOCK,
    "access_key":API_KEY2,
    "date_from":"2023-02-16T00:00:00+0000",
    "date_to":"2023-02-17T00:00:00+0000"
}

result = requests.get(NEWS_ENDPOINT, params=parameter)
result.raise_for_status()

data = result.json()
title = data['articles'][0]['title']
description = data['articles'][0]['description']

stock = requests.get(STOCK_ENDPOINT, params=params_stock)
stock.raise_for_status()

result = stock.json()
yesterday = result['data'][0]['close']
before_yes = result['data'][1]['close']

monitor = before_yes - yesterday
percentage = round((before_yes - yesterday) / before_yes * 100)

if monitor > 0:
    print(f"TSLA 🔺: {percentage}\nHeadline: {title}\nBrief: {description}")
else:
    print(f"TSLA 🔻: {percentage}\nHeadline: {title}\nBrief: {description}")

