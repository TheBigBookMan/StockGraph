# get stock prices from--- https://pypi.org/project/yfinance/

# show stock prices in a graph

# use this library for the graphs - https://plotly.com/python/financial-charts/

import yfinance as yf

ticker_chosen = input("Type in the ticker for the graph of stock price you would like to view, eg (MSFT= Microsoft, AAPL= Apple, TSLA= Tesla)")

data = yf.Ticker(f"{ticker_chosen}")

print(data.info)