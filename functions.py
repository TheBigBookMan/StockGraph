import time

def get_current_time():
  return time.strftime('%Y-%m-%d')


# * Functioon that uses the api calls and then gives back to the GUI
def api_call(ticker, start_date, end_date, timeframe):
  print(f"Ticker: {ticker} Start-Date: {start_date} End-Date: {end_date} Timeframe: {timeframe}")

# ? Function that checks if the ticker is already in the history section or not
def add_to_tickers_file(value):
  counter = 0
  with open("tickers.txt", 'r') as file:
    tickers = file.readlines()
  for ticker in tickers:
      if value == ticker[:-1]:
        counter+=1
    
  if counter < 1:
    tickers.append(value + '\n')
    with open("tickers.txt", 'w') as file:
      file.writelines(tickers)
