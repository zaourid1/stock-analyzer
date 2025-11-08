# Simple Configuration - MVP Version

# Basic settings
DEBUG = True
SECRET_KEY = "your-secret-key-here"

# Data settings
DEFAULT_PERIOD = "1y"
DEFAULT_RSI_PERIOD = float(14)
DEFAULT_MA_PERIODS = [20, 50]
DEFAULT_SMA_PERIODS = "3wk"

# Web settings
HOST = "0.0.0.0"
PORT = 5000

# Sample tickers for demo
SAMPLE_TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
