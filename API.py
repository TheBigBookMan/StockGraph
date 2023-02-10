#?  use this library for the graphs - https://plotly.com/python/financial-charts/
# https://matplotlib.org/stable/gallery/showcase/stock_prices.html

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def call_api(ticker, start_date, end_date, timeframe):
    if start_date == 'max':
        df = yf.download(tickers=ticker, end=end_date, interval=timeframe)
    else: 
        df = yf.download(ticker, start_date, end_date, interval=timeframe)


    df = df.reset_index()

    dates = []
    prices = []

    for index, row in df.iterrows():
        date = str(row[0])[:10]
        dates.append(date)
        prices.append(row[1])

    formatted_dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    graph = create_graph(formatted_dates, prices, ticker, start_date, end_date, timeframe)



def create_graph(dates, prices, ticker, start_date, end_date, timeframe):
    # # ? this is the numbers plotting, first array is the X axis (date) second array is the Y axis (price)-- need to get an array of the dates for first, and Highs for second array
    # # * can change style--- have a marker (marker='o', markersize=12)

    # ? Makes the X axis more readable
    min_price_axis = min(prices) / 4
    max_price_axis = max(prices) + (max(prices) / 8)

    # ? Formats the dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

    # ? Dynamically renders the Y axis dates according to data input
    # TODO need to make this dynamic to the timeframe selected by user-- 
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.plot(dates, prices, color='orange')
    plt.gcf().autofmt_xdate()

    # # ? axis numbers, first two are X (date), last 2 are Y (price)
    plt.ylim([min_price_axis, max_price_axis])
    # plt.xlim([start_date, end_date])

    plt.xlabel("Date-Range")
    plt.ylabel('Price')  
    plt.title(f"Ticker: {ticker} Date-Range: {start_date} / {end_date} Timeframe: {timeframe}")
    plt.show()
    
