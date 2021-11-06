# to import libraries
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi



def get_data(tickers):
    """
    Download data for the selected tickers from ALPACA API with the API keys
    stored in the 'api.env' document 
    """
    load_dotenv()
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
    
    alpaca = tradeapi.REST(
     alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")
    
    timeframe = '1D'

    start_date = pd.Timestamp("2020-06-30", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2021-10-31", tz="America/New_York").isoformat()
    
    price_df = alpaca.get_barset(
    tickers,
    timeframe,
    start = start_date,
    end = end_date
    ).df
    
    return price_df