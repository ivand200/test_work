import yfinance as yf
from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
import yahoo_fin.stock_info as si

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_ma(share, interval, ma: int):
    """
    Get
    ticker: AAPLE, MMM CCL etc.
    interval: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo,
    ma: period, integer
    and return Moving averege for this period
    """
    try:
        ticker = yf.Ticker(share)
        ticker = ticker.history(period="max", interval=f"{interval}")
        ticker = ticker[ticker["Close"].notna()]
        ticker["MA"] = ticker["Close"].rolling(ma).mean()
    except:
        return 0
    else:
        return ticker["MA"]


def get_ma_by_yahoo_fin(ticker, ma):
    try:
        ticker = si.get_data(ticker, interval="1mo")
        ticker = ticker[ticker["close"].notna()]
        ticker["MA"] = ticker["close"].rolling(ma).mean()
    except:
        return 0
    else:
        return ticker["MA"]


def get_close(ticker):
    ticker = si.get_data(ticker, interval="1mo")
    ticker = ticker[ticker["close"].notna()]
    return ticker["close"]

get_ma("AAPL", "1mo", 14).plot(legend=True)
get_close("AAPL").plot(legend=True)
plt.show()
