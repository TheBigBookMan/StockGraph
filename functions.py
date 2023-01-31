import time

def get_current_time():
  return time.strftime('%Y-%m-%d')

# * need a function for history section to add to the tickers.txt file when "searched"


# * Functioon that uses the api calls and then gives back to the GUI
def api_call(ticker, start_date, end_date, timeframe):
  print(f"Ticker: {ticker} Start-Date: {start_date} End-Date: {end_date} Timeframe: {timeframe}")