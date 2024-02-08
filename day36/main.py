import requests
from datetime import datetime, timedelta
from decouple import config

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


yesterday = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
before_yesterday = datetime.strftime(datetime.now() - timedelta(2), "%Y-%m-%d")

stock_api_key =config('STOCK_API_KEY')
news_api_key = config('NEWS_API_KEY')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

response = requests.get(stock_api, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

y_close = float(stock_data[yesterday]["4. close"])
by_close = float(stock_data[before_yesterday]["4. close"])
diff = round(y_close - by_close, 2)
percentage = round((diff / by_close) * 100, 2)

if abs(percentage) >= 0.00:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "from": before_yesterday,
        "to": yesterday,
        "language": "en",
        "pageSize": 3,
    }
    news_response = requests.get(news_api, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()["articles"]

    for article in articles:
        sign = "🔺" if percentage > 0 else "🔻"
        headline = article["title"]
        brief = article["description"]
        message = (
            f"{STOCK}: {sign}{abs(percentage)}%\nHeadline: {headline}\nBrief: {brief}\n"
        )
        print(message)

else:
    print('Nothing worthy today.')
