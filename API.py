
# ?  get stock prices from--- https://pypi.org/project/yfinance/

# ? user types in a UI what ticker they want and then it shows up a basic graph of the infor for it and then just some basic information underneath it
#? marketcap, events, link to website, name, ticker, price, percent prices maybe

#?  use this library for the graphs - https://plotly.com/python/financial-charts/
# https://matplotlib.org/stable/gallery/showcase/stock_prices.html

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ticker_chosen = input("Type in the ticker for the graph of stock price you would like to view, eg (MSFT= Microsoft, AAPL= Apple, TSLA= Tesla)")
# data = yf.Ticker(f"{ticker_chosen}")

#!!!! TEMPORARY TESLA SO DONT HAV ETO INPUT EVERYTIME

def call_api(ticker, start_date, end_date, timeframe):
    df = yf.download(ticker, start_date, end_date, interval=timeframe)
    df = df.reset_index()

    dates = []
    prices = []

    for index, row in df.iterrows():
        date = str(row[0])[:10]
        dates.append(date)
        prices.append(row[1])

    # print(dates)
    # print(prices)

    graph = create_graph(dates, prices, ticker, start_date, end_date, timeframe)



def create_graph(dates, prices, ticker, start_date, end_date, timeframe):
    # # ? this is the numbers plotting, first array is the X axis (date) second array is the Y axis (price)-- need to get an array of the dates for first, and Highs for second array
    # # * can change style--- have a marker (marker='o', markersize=12)

    date_axis = dates[::100]
    # print(date_axis)

    plt.plot(dates, prices, color='orange')
    plt.xticks(range(min(dates), max(dates)+100, 1.0))

    min_price_axis = min(prices) / 4
    max_price_axis = max(prices) + (max(prices) / 8)


    # # ? axis numbers, first two are X (date), last 2 are Y (price)
    # plt.ylim([min_price_axis, max_price_axis])
    # plt.xlim([start_date, end_date])

    plt.xlabel(timeframe)
    plt.ylabel('Price')  
    plt.title(f"Ticker: {ticker} Date-Range: {start_date} / {end_date} Timeframe: {timeframe}")
    plt.show()
    
