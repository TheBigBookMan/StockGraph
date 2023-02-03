import PySimpleGUI as sg
import os
import functions

# TODO add in a history section for previous selected stock tickers where adding in any searched tickers get added to the text file--- can just be a random txt file

# TODO add in fcuntion to do todays date

# TODO create a theme-- google: PySimleGUI themes-- go on geeksforgeeks website

# TODO maybe add images to the buttons to make it look a bit better, search maybe with a magnifying glass
# todo might need to change mouseover_color for the button change colour and a tooltip for extra info

# TODO link up with the functions from API call and then information is sent back

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
daily_period = sg.Radio("Daily", "TIMEFRAME", default=True, key="daily")
weekly_period = sg.Radio("Weekly", "TIMEFRAME",  default=False, key="weekly")
monthly_period = sg.Radio("Monthly", "TIMEFRAME", default=False, key="monthly")
yearly_period = sg.Radio("Yearly", "TIMEFRAME", default=False, key="yearly")

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

# ? Creating the layout structure of the GUI
layout = [
    [title_info],
    [ticker, ticker_input],
    [start_date, start_date_input, start_date_button, max_historical_date],
    [end_date, end_date_input, end_date_button, end_date_today],
    [period_title],
    [daily_period, weekly_period, monthly_period, yearly_period],
    [submit_button, exit_button, user_selection],
    [listbox]
    ],

window = sg.Window('StockGraph', layout=layout, size=(1200, 600))

while True:
    event, values = window.read()

    # TODO selection of favourite can then be used as ticker

    # todo window['ticker'].update(value={return value from the function of selecting the historical one})-- this takes the value clicked in the history section and then adds it to the ticker input box ready to be used in search

    # todo sg.popup()--- use this for any errors eg- blank inputs, no api from wrong tiker etc
    # todo use above with try except problems

    #  TODO add in conditionals so user fills in correct information into the inputs
    
    

    if sg.WIN_CLOSED:
        break
    elif event == 'exit_program':
        break
    elif event == "today_date":
        window['end_date'].update(value=functions.get_current_time())
    elif event == "max_date":
        window['start_date'].update(value="max")
        window['end_date'].update(value="max")
    elif event == 'search_button':
        if values['daily'] == True:
            timeframe = 'daily'
        if values['weekly'] == True:
            timeframe = 'weekly'
        if values['monthly'] == True:
            timeframe = 'monthly'
        if values['yearly'] == True:
            timeframe = 'yearly'

        # TODO maybe have a try except for the api call and the except can have red text show up

        if values['list_box']:
            ticker = str(values['list_box'][0].strip('\n'))
        else:  
            functions.add_to_tickers_file(values['ticker'])
        
        functions.api_call(ticker, values['start_date'], values['end_date'], timeframe)
        window['user_selection'].update(f"Ticker: {ticker} Date-Range: {values['start_date']} / {values['end_date']} Timeframe: {timeframe}")

window.close()