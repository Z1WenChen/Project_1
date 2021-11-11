# to import libraries
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import numpy as np



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

    start_date = pd.Timestamp("2018-10-31", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2021-10-31", tz="America/New_York").isoformat()
    
    price_df = alpaca.get_barset(
    tickers,
    timeframe,
    start = start_date,
    end = end_date
    ).df
    
    return price_df

def asset_return(asset):
    return_df = asset.pct_change().dropna()
    return return_df

def annualize_rets(r, periods_per_year):
    """
    Annualizes a set of returns
    """
    compounded_growth = (1+r).prod()
    n_periods = r.shape[0]
    return compounded_growth**(periods_per_year/n_periods)-1

def portfolio_return(weights, returns):
    """
    Weights -> Portfolio Returns
    """
    return weights.T @ returns

def portfolio_vol(weights,covmat):
    """
    Weights -> Vol
    """
    return (weights.T @ covmat @ weights)**0.5

def ef2(n_points, er, cov):
    """
    Plots the 2-asset efficient frontier
    """

    weights = [np.array([w, 1-w]) for w in np.linspace(0, 1, n_points)]
    
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({
        "Returns": rets,
        "Volatility": vols
    })
    return ef