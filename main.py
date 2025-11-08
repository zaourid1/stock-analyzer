'''
Stock Analyzer Bot - Simple MVP Version

Core features only:
1. Fetch stock data
2. Calculate basic indicators (RSI, Moving Averages)
3. Generate buy/sell signals
4. Simple web dashboard
'''

import pandas as pd
from datetime import datetime
from data_fetcher import get_stock_data, validate_ticker
from analysis import calculate_rsi, calculate_moving_averages, generate_signal
#from web import run_web_app
import config
import yfinance as yf

class StockAnalyzer:
    """Simple stock analyzer - MVP version"""
    
    def __init__(self):
        """Initialize the analyzer with default settings"""
        self.debug = config.DEBUG
        self.default_period = config.DEFAULT_PERIOD
        self.rsi_period = config.DEFAULT_RSI_PERIOD
        self.ma_periods = config.DEFAULT_MA_PERIODS
        self.sma_periods = config.DEFAULT_SMA_PERIODS
        
        # Store analysis results
        self.current_analysis = {}
    
    def analyze_stock(self, ticker, period="1y"):
        """Analyze a single stock"""
        # Ensure ticker is a string and convert to uppercase
        if not isinstance(ticker, str):
            raise TypeError(f"ticker must be a string, got {type(ticker)}")
        ticker = ticker.upper()
        print("Stock Analysis")
        rsi = calculate_rsi(ticker)
        print("RSI: ")
        print(rsi)
        sma = calculate_moving_averages(ticker,period=self.sma_periods)
        print("Moving Averages: ")
        print(sma)
        return
    
    def analyze_multiple_stocks(self, tickers):
        """Analyze multiple stocks"""
        pass
    
    def run_web_interface(self):
        """Start the web interface"""
        pass

def main():
    print("📈 WELCOME TO STOCK ANALYZER ZINEB!")
    
    while True:
        ticker = input("enter a stock: ").strip().upper()

        if not validate_ticker(ticker):
            print("❌ Invalid stock ticker. Try again.\n")
            continue  # go back to start of loop

        # If we’re here, ticker is valid AND has data
        #Builds a Ticker Object
        stock = yf.Ticker(ticker)
        
        hist = stock.history(period="1d")

        latest_close = hist["Close"].iloc[-1]
        print(f"✅ {ticker} is valid.")
        print(f"💵 Last close: {latest_close}")

        a = StockAnalyzer()
        a.analyze_stock(ticker, period=config.DEFAULT_PERIOD)
        break  # exit the loop after success




if __name__ == "__main__":
    main()