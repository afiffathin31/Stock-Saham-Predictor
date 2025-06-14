import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def download_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    return df[['Close']]

def scale_data(df, window):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)

    X, y = [], []
    for i in range(window, len(scaled)):
        X.append(scaled[i-window:i])
        y.append(scaled[i])

    return np.array(X).reshape(-1, window, 1), np.array(y), scaler
