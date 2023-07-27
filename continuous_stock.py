import asyncio
import os
import pandas as pd
import yfinance as yf
from collections import deque
from datetime import datetime
from pathlib import Path
from util_logger import setup_logger

logger, log_filename = setup_logger(_file_)

def get_API_key():
    load_dotenv()
    key = os.getenv("OPEN_WEATHER_API_KEY")
    return key

def lookup_ticker(company):
   stocks_dictionary = {
        "Tesla Inc": "TSLA",
        "General Motors Company": "GM",
        "Toyota Motor Corporation": "TM",
        "Ford Motor Company": "F",
        "Honda Motor Co": "HMC",
    } 
   return "F"
   
async def get_stock_price(ticker):
    logger.info("Calling get_stock_price for {ticker}}")
    # stock = yf.Ticker(ticker) # Get the stock data
    # price = stock.history(period="1d").tail(1)["Close"][0] # Get the closing price
    price = randint(132, 148) 
    return price
