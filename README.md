# StockGraph

## Introduction

This is a simple GUI application where users can input certain criteria for a US stock, and then they will be able to view a price chart based on the input. The ticker they choose to search for will be saved and used later if they would like.

## GitHub Repo

https://github.com/TheBigBookMan/StockGraph

## Technologies

Python, PySimpleGui, MatPlotLib, PyPlot, Yahoo Finance Third Party API and PyInstaller.

## Initialization

In root folder to open application-- Currently working on making it a .exe file

```
python gui.py
```

## Functionality

### GUI

The graphical user interface is created by using the Python library PySimpleGui and then the layout is built on top with a backend created in Python as well.

### Search Form

The user can input a US stock ticker, a start date, end date and the timeframe they want for each stock. The ticker is the basic tickers from US (Apple = AAPL, Amazon = AMZN etc) and then these are stored in a .txt file on the local users computer. The start date can be a selected formatted date in the search bar, using the calendar "Start Date" or clicking "Max Date" for the stock be from the first date it was open. The end date can also be typed in within the search bar, using the calendar "End Date" or clicking "Today's Date" for the most present date. The timeframe can be selected for daily, weekly or monthly.

### History

The .txt file that is created on the local users computer will be a mini database just for the ticker names to be used. This is created as a history section, so the user doesnt have to repeatedly input the Stock tickers.

### API

This application is using the Yahoo Finance API which responds with stock price data based on the criteria input by the user.

### Graph

The graph uses MatPLotLib and PyPlot with the data taken from the Yahoo Finance API. This is then sorted into a presentable manner that can be shown on the graph in an easy way.

![](/StockGraph.png)
