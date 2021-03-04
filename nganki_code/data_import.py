#!/usr/bin/env python3
"""
This module hosts all functions used to import data in the Nganki project.
REMEMBER TO REMOVE UNWANTED HASH MARKS AT THE END
"""
import requests
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import yfinance as yf
import fredapi as fred

# Download Swiss equity data
url_six_eq = ('https://www.six-group.com/sheldon/' +
'equity_issuers/v1/equity_issuers.csv')
six_eq = requests.get(url_six_eq)

with open('six_eq.csv', 'wb') as f:
    f.write(six_eq.content)

col_list = ['Symbol']
six_eq_symbols = pd.read_csv('six_eq.csv', delimiter=';', usecols=col_list)
# Necessary for Yahoo Finance
#six_eq_symbols = six_eq_symbols['Symbol'].astype(str) + '.SW'
six_eq_symbols = ['ABBN.SW', 'BAER.SW', 'MMM.SW']

# Set time parameters and dataframe
end_date = dt.datetime.now().date() - dt.timedelta(days=1)
start_date = end_date - dt.timedelta(days=365)
date_range = pd.date_range(str(start_date), str(end_date))

# Download and format Yahoo Finance data
# In a loop, as some tickers may not be available
six_eq_yahoo = pd.DataFrame(date_range, columns=['Date'])
for ticker in six_eq_symbols:
    try:
        df = yf.download(ticker, start_date, end_date, interval='1d')['Adj Close']
        df = df.rename(ticker)
        df = df.reset_index()
        six_eq_yahoo = pd.merge(six_eq_yahoo, df, on='Date', how='outer')
    except Exception:
        pass

# Download spot risk-free return -- TO BE COMPLETED

six_eq_yahoo = six_eq_yahoo.set_index('Date')
six_eq_yahoo = six_eq_yahoo.dropna(how='all')

if __name__ == '__main__':
    print(six_eq_yahoo)
    pass
