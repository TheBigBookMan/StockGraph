import PySimpleGUI as sg
import os
import functions
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# TODO add in a button to download the data to a folder or send an email of the graph to an email address???

sg.theme("LightBlue2")

# ? Might need to make a file for the tickers history-- for users who do not have the tickers.txt
if not os.path.exists('tickers.txt'):
    with open('tickers.txt', 'w') as file:
        pass

title_info = sg.Text("Welcome to StockGraph! Input details below and then a graph will be shown for the stock you are tracking.")

#  ? Get the users input for ticker
ticker = sg.Text("Ticker: ")
ticker_input = sg.InputText(tooltip='Input ticker', key='ticker')

# ? Get the users input for start and end dates in format
start_date = sg.Text("Start date (YYYY-MM-DD): ")
start_date_input = sg.InputText(tooltip='Start Date', key='start_date')
start_date_button = sg.CalendarButton("Start Date", key='start_date_button', format='%Y-%m-%d')
# ? Button to get the max historical date
max_historical_date = sg.Button("Max Date", key="max_date")
end_date = sg.Text("End date (YYYY-MM-DD): ")
end_date_input = sg.InputText(tooltip='End Date', key='end_date')
end_date_button = sg.CalendarButton("End Date", key='end_date_button', format='%Y-%m-%d')
# ? Button to link up to a function that gets todays date for the input
end_date_today = sg.Button("Today's Date", key='today_date')

# ? List of time periods
period_title = sg.Text("Select timeframe: ")
period_description = sg.Text("This is for the amount of plots and detail on the graph.")
daily_period = sg.Radio("Daily", "TIMEFRAME", default=True, key="daily")
weekly_period = sg.Radio("Weekly", "TIMEFRAME",  default=False, key="weekly")
monthly_period = sg.Radio("Monthly", "TIMEFRAME", default=False, key="monthly")

# ? Search button will connect to the function other file and call the API
submit_button = sg.Button("Search", key='search_button')

# ? Exit program button
exit_button = sg.Button("Exit", key='exit_program')

# ? Display what user chose
user_selection = sg.Text("", key="user_selection", text_color="Blue")

# ? Getting the list of favourites from text file
with open('tickers.txt', 'r') as file:
    tickers = file.readlines()

# ? Listbox functon for the list of the ticker history from a txt file that has the ticker history stored
listbox = sg.Listbox(tickers, size=(10, 30), key="list_box")

# ? Canvas layout for graph
canvas = sg.Canvas(size=(1000, 600), key="-CANVAS-")

# ? Creating the layout structure of the GUI
layout = [
    [title_info],
    [ticker, ticker_input],
    [start_date, start_date_input, start_date_button, max_historical_date],
    [end_date, end_date_input, end_date_button, end_date_today],
    [period_title],
    [period_description],
    [daily_period, weekly_period, monthly_period],
    [submit_button, exit_button, user_selection],
    [listbox, canvas]
    ],

window = sg.Window('StockGraph', layout=layout, size=(1200, 650), finalize=True, resizable=True)
# * Maybe add in finalize=True

fig, ax = plt.subplots()
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack(side='bottom', fill='both', expand=1)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'exit_program':
        break
    elif event == "today_date":
        window['end_date'].update(value=functions.get_current_time())
    elif event == "max_date":
        window['start_date'].update(value="max")
        start_date = 'max'
    elif event == 'search_button':
        if values['daily'] == True:
            timeframe = '1d'
        elif values['weekly'] == True:
            timeframe = '1wk'
        elif values['monthly'] == True:
            timeframe = '1mo'

        if values['list_box']:
            ticker = str(values['list_box'][0].strip('\n'))
        else:  
            ticker = values['ticker']
        
        try:
            graph_data = functions.api_call(ticker, values['start_date'], values['end_date'], timeframe)
            window['user_selection'].update(f"Ticker: {ticker} Date-Range: {values['start_date']} / {values['end_date']} Timeframe: {timeframe}")
            

            # window['-CANVAS-'].TKCanvas.get_tk_widget.forget()
            # TODO if statement for something with the window[canvas] that checks if there is an image in there and then if there is then it removes the pack 'canvas.get_tk_widget().pack_forget()'---- not cavnas though because aint working SOEMTHING--- then call draw figure
            figure_canvas_agg.get_tk_widget().pack_forget()
            figure_canvas_agg = functions.draw_figure(window['-CANVAS-'].TKCanvas, graph_data, figure_canvas_agg)
            functions.add_to_tickers_file(values['ticker'])

        except ValueError:
            sg.popup("That ticker didn't work, please try again...")

window.close()