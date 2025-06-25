import os
import requests
from dotenv import load_dotenv
from utils import log_action

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey="
STOCK_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey="