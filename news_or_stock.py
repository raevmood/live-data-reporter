import os
import requests
from dotenv import load_dotenv
from utils import log_action

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey="
STOCK_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey="

def fetch_news_or_stock():
    print("\nChoose data source:")
    print("1. Top 3 US business headlines")
    print("2. IBM stock 5-min open price")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            response = requests.get(NEWS_URL + NEWS_API_KEY)
            response.raise_for_status()
            articles = response.json().get("articles", [])
            print("\nTop 3 Business Headlines:")
            for article in articles:
                print(f"- {article['title']}")
            log_action("News fetched", "Success")
        except Exception as e:
            log_action("News fetch", f"Failed: {e}")
            print(f"Error: {e}")
    elif choice == '2':
        try:
            response = requests.get(STOCK_URL + STOCK_API_KEY)
            response.raise_for_status()
            data = response.json()
            times = list(data["Time Series (5min)"].keys())
            latest_time = times[0]
            open_price = data["Time Series (5min)"][latest_time]["1. open"]
            print(f"\nIBM Stock (5-min) Open Price: ${open_price} at {latest_time}")
            log_action("Stock data fetched", "Success")
        except Exception as e:
            log_action("Stock fetch", f"Failed: {e}")
            print(f"Error: {e}")
    else:
        print("Invalid choice.")
