# ?  get stock prices from--- https://pypi.org/project/yfinance/

# ? user types in a UI what ticker they want and then it shows up a basic graph of the infor for it and then just some basic information underneath it
#? marketcap, events, link to website, name, ticker, price, percent prices maybe

#?  use this library for the graphs - https://plotly.com/python/financial-charts/
# https://matplotlib.org/stable/gallery/showcase/stock_prices.html

#  TODO ust the PySimpleGUI library to make an easy GUI for users to input data liuke ticket etc and then use Pandas etc to show the graph

import yfinance as yf

# !!
# !! RATHER THAN USE THE API, could use a web scraper like beautiful soup to download the csv file and then use a Pandas library to get the data and store it better into matplot lib---- good practice for web scraping and pandas
# !!


# ticker_chosen = input("Type in the ticker for the graph of stock price you would like to view, eg (MSFT= Microsoft, AAPL= Apple, TSLA= Tesla)")
# data = yf.Ticker(f"{ticker_chosen}")

#!!!! TEMPORARY TESLA SO DONT HAV ETO INPUT EVERYTIME

def call_api(ticker, start_date, end_date, timeframe):
    data = yf.download(ticker, start_date, end_date, interval=timeframe)
    print(data)

    # data_history = data.history(start=start_date, end=end_date)
    # data_info = data.info
    # data_news = data.news

    # print(data_info)
    # print(data_history)
    # print(data_news)

