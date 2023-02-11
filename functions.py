import time
import API
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_current_time():
  return time.strftime('%Y-%m-%d')

def draw_figure(canvas, figure, figure_canvas_agg):
    # figure_canvas_agg.get_tk_widget().destroy()
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    # print(figure_canvas_agg)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='bottom', fill='both', expand=1)
    return figure_canvas_agg


# * Functioon that uses the api calls and then gives back to the GUI
def api_call(ticker, start_date, end_date, timeframe):
  graph_data = API.call_api(ticker, start_date, end_date, timeframe)
  return graph_data

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
