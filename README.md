# 🧠 StockAnalyzer
**ML-Powered Market Insight & Trading Strategy System + Technical Indicator Bot (Hybrid)**
A modular Python project that fetches, analyzes, and visualizes stock market data to generate algorithmic trading signals — bridging **data science, finance, and software engineering**.

## 🚀 Overview
**StockAnalyzer** automates the process of collecting real-time and historical stock data from Yahoo Finance, analyzing it with technical indicators, generating trading signals, and visualizing performance metrics.

## 🧩 Architecture
main.py → data_fetcher.py → analysis.py → strategy.py → visualizer.py → notifier.py

## ⚙️ Features
- Fetches live and historical stock data
- Cleans data, computes indicators (RSI, MACD, SMA, Bollinger Bands)
- Implements algorithmic strategies with backtesting
- Visualizes buy/sell signals and portfolio performance
- Optional alert system for trade notifications

## 🧠 Technology Stack
Python · yfinance · Polygon.io · pandas · numpy · matplotlib · plotly

## 📊 Example Strategy
If (SMA_20 > SMA_50) and (RSI < 60): → BUY
If (SMA_20 < SMA_50) or (RSI > 70): → SELL

## 🧪 Backtesting Metrics
- Cumulative Returns
- Max Drawdown
- Sharpe Ratio
- Accuracy (Win Rate)
- Volatility vs. Market Benchmark

## 📂 Folder Structure
src/
 ├── main.py
 ├── data_fetcher.py
 ├── analysis.py
 ├── strategy.py
 ├── visualizer.py
 ├── notifier.py
 ├── config.json
 └── requirements.txt

## 🎓 Learning Value
- Demonstrates real-world API integration and data engineering
- Applies quantitative finance and algorithmic strategy design
- Extendable to ML-based predictive models and real-time trading

## 📜 License
Open-source project for educational and research use only.
