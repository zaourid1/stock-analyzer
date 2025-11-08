'''
Simple Data Fetcher - MVP Version

Core functionality only:
- Fetch stock data from Yahoo Finance
- Basic data validation
'''

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def get_stock_data(ticker, period="1y"):
    """
    Get stock data for a ticker
    
    Args:
        ticker (str): Stock symbol (e.g., 'AAPL')
        period (str): Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
    
    Returns:
        pandas.DataFrame: OHLCV data - 
        Note: YFinance Data alr comes in a dataframe
    """
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    start_date = "2025-10-01"
    end_date = datetime.today()
    #start_date = end_date - pd.DateOffset(intervals)
    stock_historical = stock.history(start=start_date, end=end_date, interval='1wk')

    #df = pd.DataFrame(stock_histoical)
    return stock_historical

def get_current_price(ticker):
    """
    Get current price for a ticker
    
    Args:
        ticker (str): Stock symbol
    
    Returns:
        float: Current price
    """
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    rounded = round(stock.fast_info['lastPrice'], 2)
    return rounded

def get_multiple_stocks(tickers, period="1y"):
    """
    Get data for multiple stocks
    
    Args:
        tickers (list): List of stock symbols
        period (str): Time period
    
    Returns:
        dict: Dictionary with ticker as key and data as value
    """
    # Uppercase all tickers if they're strings
    if isinstance(tickers, list):
        tickers = [t.upper() if isinstance(t, str) else t for t in tickers]
    elif isinstance(tickers, str):
        tickers = tickers.upper()
    data = yf.download(tickers, start="2025-10-01", end=datetime.today())
    return data

def validate_ticker(ticker: str) -> bool:
    ticker = ticker.upper().strip()
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")  # latest daily data
        # If no rows, it's not usable
        if hist.empty:
            return False
        # If Close column exists but is all NaN, also useless
        if "Close" not in hist.columns:
            return False
        if hist["Close"].isna().all():
            return False
        return True
    except Exception:
        # yfinance blew up (network issue, nonsense ticker, etc.)
        return False
    
def rsi_prices(ticker):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    
    stock_data = stock.history(period='1mo')
    close_prices = stock_data['Close']
    rsi_change = []
    #print("CLOSE PRICES")
    #print(close_prices)
    if len(close_prices) < 14:
        # Not enough data points, handle gracefully
        list(close_prices)
        #print("not enough data points")
    
    for i in range(14):
        if i == 0:
            change = close_prices.iloc[i]
            rsi_change.append(change)
        else:
            change =  close_prices.iloc[i] - close_prices.iloc[i-1]
            rsi_change.append(change)
        #print('RS: ', rsi_change)
    
    #df = pd.DataFrame(stock_histoical)
    #print('ehat the helly')
    rsi_gains = []
    rsi_loss = []
    for v in rsi_change:
        if v < 0:
            rsi_loss.append(round(v,2))
        else:
            rsi_gains.append(round(v,2))
    print("---------RSI GAINS------------")
    print(np.array(rsi_gains))
    print("---------RSI LOSSES------------")
    print(np.array(rsi_loss))

    sum_gains = float(abs(sum(rsi_gains)))
    sum_loses = float(abs(sum(rsi_loss)))

    print(sum_gains)
    print(sum_loses)
    return sum_gains, sum_loses

def sma_prices(ticker, period):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    
    stock_data = stock.history(period=period)
    close_prices = stock_data['Close']

    return close_prices


