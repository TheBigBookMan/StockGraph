# ?  get stock prices from--- https://pypi.org/project/yfinance/

# ? user types in a UI what ticker they want and then it shows up a basic graph of the infor for it and then just some basic information underneath it
#? marketcap, events, link to website, name, ticker, price, percent prices maybe

#?  use this library for the graphs - https://plotly.com/python/financial-charts/

# TODO make a front end so users can input and view things
#  TODO ust the PySimpleGUI library to make an easy GUI for users to input data liuke ticket etc and then use Pandas etc to show the graph

import yfinance as yf




# ticker_chosen = input("Type in the ticker for the graph of stock price you would like to view, eg (MSFT= Microsoft, AAPL= Apple, TSLA= Tesla)")
# data = yf.Ticker(f"{ticker_chosen}")

#!!!! TEMPORARY TESLA SO DONT HAV ETO INPUT EVERYTIME
data = yf.Ticker("TSLA")

data_history = data.history(start="2017-01-01", end="2017-04-30")
data_calendar = data.calendar
data_info = data.info
data_news = data.news

# print(data.info)
# print(data_history)
# print(data_calendar)
# print(data_news)

