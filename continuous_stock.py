import asyncio
import os
import pandas as pd
import yfinance as yf
from collections import deque
from datetime import datetime
from random import randint
from dotenv import load_dotenv
from pathlib import Path
from util_logger import setup_logger

logger, log_filename = setup_logger(__file__)


def get_API_key():
    # Keep secrets in a .env file - load it, read the values.
    # Load environment variables from .env file
    load_dotenv()
    key = os.getenv("OPEN_STOCK_API_KEY")
    return key


def lookup_ticker(company):
   stocks_dictionary = {
        "Tesla Inc": "TSLA",
        "General Motors Company": "GM",
        "Toyota Motor Corporation": "TM",
        "Ford Motor Company": "F",
        "Honda Motor Co": "HMC",
    } 
   ticker = stocks_dictionary(company)
   return ticker
   
async def get_stock_price(ticker):
    logger.info(f"Calling get_stock_price for {ticker}")
    # stock = yf.Ticker(ticker)
    # price = stock.info["currentPrice"]
    price = randint(132, 148)
    return price

# Create or overwrite CSV with column headings
def init_stock_csv_file(file_path):
    df_empty = pd.DataFrame(columns=["Company", "Ticker", "Time", "Stock_Price"])
    df_empty.to_csv(file_path, index=False)


async def update_csv_stock():
    """Update the CSV file with the latest stock prices."""
    logger.info("Calling update_csv_stock")

    try:
        # Add column headers when creating the empty CSV file for stock prices
        file_path = Path(__file__).parent.joinpath("data").joinpath("mtcars_stock.csv")
        if not os.path.exists(file_path):
            df_empty = pd.DataFrame(
                columns=["Company", "Ticker", "Time", "Price"]
            ).copy()
            df_empty.to_csv(file_path, index=False)

        # Stub: Create a simple DataFrame with static data
        df_data = pd.DataFrame({
            "Company": ["Tesla Inc", "General Motors Company"],
            "Ticker": ["TSLA", "GM"],
            "Time": ["2023-07-25 12:00:00", "2023-07-25 12:01:00"],
            "Price": [700.0, 60.0]
        })

        # Save stock prices to the CSV file
        logger.info(f"Saving stock prices to {file_path}")
        df_data.to_csv(file_path, index=False)

    except Exception as e:
        logger.error(f"An error occurred in update_csv_stock: {e}")