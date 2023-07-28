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


# Writes new stock info to CSV
async def update_csv_stock():
    logger.info("Calling update_csv_stock")
    try:
        companies = [
            "Tesla Inc",
            "General Motors Company",
            "Toyota Motor Corporation",
            "Ford Motor Company",
            "Honda Motor Co",
        ]
        update_interval = 60  # Update every 1 minute (60 seconds)
        total_runtime = 15 * 60  # Total runtime maximum of 15 minutes
        num_updates = 10  # Keep the most recent 10 readings
        logger.info(f"update_interval: {update_interval}")
        logger.info(f"total_runtime: {total_runtime}")
        logger.info(f"num_updates: {num_updates}")

        # Use a deque to store just the last, most recent 10 readings in order
        records_deque = deque(maxlen=num_updates)

        fp = Path(__file__).parent.joinpath("data").joinpath("mtcars_stock.csv")

        # Check if the file exists, if not, create it with only the column headings
        if not os.path.exists(fp):
            init_stock_csv_file(fp)

        logger.info(f"Initialized csv file at {fp}")

        for _ in range(num_updates):  # To get num_updates readings
            for company in companies:
                ticker = lookup_ticker(company)
                new_price = await get_stock_price(ticker)
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
                new_record = {
                    "Company": company,
                    "Ticker": ticker,
                    "Time": time_now,
                    "Price": new_price,
                }
                records_deque.append(new_record)

            # Use the deque to make a DataFrame
            df = pd.DataFrame(records_deque)

            # Save the DataFrame to the CSV file, deleting its contents before writing
            df.to_csv(fp, index=False, mode="w")
            logger.info(f"Saving prices to {fp}")

            # Wait for update_interval seconds before the next reading
            await asyncio.sleep(update_interval)

    except Exception as e:
        logger.error(f"ERROR in update_csv_stock: {e}")