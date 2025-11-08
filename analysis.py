'''
Simple Analysis - MVP Version

Core indicators only:
- RSI (Relative Strength Index)
- Moving Averages
- Basic buy/sell signals
'''

import pandas as pd
import numpy as np
from data_fetcher import rsi_prices, sma_prices
import config
import yfinance as yf

def calculate_rsi(ticker):
    """
    Calculate RSI (Relative Strength Index)
    
    Args:
        prices (pandas.Series): Price data
        period (int): RSI period (default 14)
    
    Returns:
        pandas.Series: RSI values
    """
    period = config.DEFAULT_RSI_PERIOD
    sum_gains, sum_loses = rsi_prices(ticker)

    avg_gain = sum_gains/period
    avg_loss = sum_loses/period
    if avg_gain == 0:
        rsi = 0
        return rsi
    
    if avg_loss == 0:
        rsi = 100
        return rsi
    rs = avg_gain/avg_loss

    rsi = 100 - (100/(1+rs))

    print(f"avg gain: {avg_gain}")
    print(f"avg loss: {avg_loss}")
    print(f"RS: {rs}")
    print(f"RSI: {rsi}")
    print()

    return rsi
    

def calculate_moving_averages(ticker, period):
    """
    Calculate Simple Moving Average
    
    Args:
        prices (pandas.Series): Price data
        period (int): Moving average period
    
    Returns:
        pandas.Series: Moving average values
    """
    prices = sma_prices(ticker,period)

    n = len(prices)

    sum_prices = np.sum(prices)

    sma = sum_prices/n
    return sma

def calculate_macd(prices, fast=12, slow=26, signal=9):
    """
    Calculate MACD (Moving Average Convergence Divergence)
    
    Args:
        prices (pandas.Series): Price data
        fast (int): Fast EMA period
        slow (int): Slow EMA period
        signal (int): Signal line EMA period
    
    Returns:
        dict: MACD line, signal line, histogram
    """
    pass

def generate_signal(data):
    """
    Generate simple buy/sell signal based on RSI and Moving Averages
    
    Args:
        data (pandas.DataFrame): Stock data with indicators
    
    Returns:
        str: 'BUY', 'SELL', or 'HOLD'
    """
    pass

def calculate_volatility(prices, period=20):
    """
    Calculate rolling volatility
    
    Args:
        prices (pandas.Series): Price data
        period (int): Rolling period
    
    Returns:
        pandas.Series: Volatility values
    """
    pass

def calculate_support_resistance(data, window=20):
    """
    Calculate simple support and resistance levels
    
    Args:
        data (pandas.DataFrame): OHLC data
        window (int): Lookback window
    
    Returns:
        dict: Support and resistance levels
    """
    pass