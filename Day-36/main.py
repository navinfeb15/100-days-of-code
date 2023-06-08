# Import necessary libraries
import os
import time
import requests
from twilio.rest import Client
from datetime import datetime, timedelta

# Set constant variables
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "TQZTV6JCKFUSPFOW"
NEWS_API_KEY = "5db26a6b22994d19b74e869ea818c216"
account_sid = "AC70c2d9568e8697cc25467fb084e74034"
auth_token = os.environ.get("TW_AUTH_TOKEN")

# Get stock data from Alpha Vantage API
today = datetime.today()
yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_yesterday = (today - timedelta(days=2)).strftime("%Y-%m-%d")
stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}
response = requests.get("https://www.alphavantage.co/query", params=stock_parameters).json()
yesterday_closing = float(response["Time Series (60min)"][f"{yesterday} 19:00:00"]["4. close"])
day_before_yesterday_closing = float(response["Time Series (60min)"][f"{day_before_yesterday} 19:00:00"]["4. close"])

# Calculate percentage change in stock price
change = ("🔺" if day_before_yesterday_closing < yesterday_closing else "🔻", abs(abs(yesterday_closing) - abs(day_before_yesterday_closing)))
percentage = (change[1] / day_before_yesterday_closing) * 100

# Check if percentage change is greater than or equal to 1%
if percentage >= 5:
    # Get news data from News API
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    NEWS_URL = "https://newsapi.org/v2/everything"
    news_json = requests.get(url=NEWS_URL, params=news_parameters).json()
    news_slice = news_json["articles"][0:3]

    # Loop through news and send messages to phone number
    for news in news_slice:
        message_content = f"""
        TSLA: {change[0]} {percentage}
        Headline: {news["title"]} [{STOCK}]
        Brief: {news["description"]}"""
        # Send message to phone number
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_content,
            from_='+14849699513',  # Your Twilio phone number
            to='+917338961810'  # The recipient's phone number
        )
        time.sleep(1)  # Avoid hitting the API too frequently