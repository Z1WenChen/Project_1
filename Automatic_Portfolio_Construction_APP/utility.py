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

def efN(n_points, er, cov, numberOfTickers):
    """
    Plots the n-asset efficient frontier
    """

    weights = []

    if numberOfTickers == 2:
        weights = [np.array([w, 1-w]) for w in np.linspace(0, 1, n_points)]
    if numberOfTickers == 3:
        weights = [np.array([w, ww, 1 - w - ww]) for w in np.linspace(0, 1, n_points) for ww in np.linspace(0, 1 - w, n_points)]
    if numberOfTickers == 4:
        weights = [np.array([w, ww, 1 - w - ww, 1 - w - ww - www]) for w in np.linspace(0, 1, n_points) for ww in np.linspace(0, 1 - w, n_points) for www in np.linspace(0, 1 - w - ww, n_points) ]
    if numberOfTickers == 5:
        weights = [np.array([w, ww, 1 - w - ww, 1 - w - ww - www, 1 - w - ww - wwww]) for w in np.linspace(0, 1, n_points) for ww in np.linspace(0, 1 - w, n_points) for www in np.linspace(0, 1 - w - ww, n_points) for wwww in np.linspace(0, 1 - w - ww - www, n_points)]
    
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({
        "Returns": rets,
        "Volatility": vols
    })
    return ef