import PySimpleGUI as sg

# TODO add in a history section for previous selected stock tickers--- can just be a random txt file

# TODO add in fcuntion to do todays date

# TODO link up with the functions from API call and then information is sent back

title_info = sg.Text("Welcome to StockGraph! Input details below and then a graph will be shown for the stock you are tracking.")

#  ? Get the users input for ticker
ticker = sg.Text("Ticker: ")
ticker_input = sg.InputText(tooltip='Input ticker', key='ticker')

# ? Get the users input for start and end dates in format
start_date = sg.Text("Start date (YYYY-MM-DD): ")
start_date_input = sg.InputText(tooltip='Start Date', key='start_date')
end_date = sg.Text("End date (YYYY-MM-DD): ")
end_date_input = sg.InputText(tooltip='End Date', key='end_date')

# ? List of time periods
period_title = sg.Text("Select timeframe: ")
daily_period = sg.Radio("Daily", "TIMEFRAME", default=True, key="daily")
weekly_period = sg.Radio("Weekly", "TIMEFRAME",  default=False, key="weekly")
monthly_period = sg.Radio("Monthly", "TIMEFRAME", default=False)
yearly_period = sg.Radio("Yearly", "TIMEFRAME", default=False)

# ? Button to link up to a function that gets todays date for the input
end_date_today = sg.Button("Today's Date")

# ? Search button will connect to the function other file and call the API
submit_button = sg.Button("Search")

# ? Getting the list of favourites from text file
with open('tickers.txt', 'r') as file:
    tickers = file.readlines()

# ? Listbox functon for the list of the ticker history from a txt file that has the ticker history stored
listbox = sg.Listbox(tickers, size=(10, 30))

# ? Creating the layout structure of the GUI
layout = [
    [title_info],
    [ticker, ticker_input],
    [start_date, start_date_input],
    [end_date, end_date_input, end_date_today],
    [period_title],
    [daily_period, weekly_period, monthly_period, yearly_period],
    [submit_button],
    [listbox]
    ],

window = sg.Window('StockGraph', layout=layout, size=(1200, 600))

while True:
    event, values = window.read()

    # TODO selection of favourite can then be used as ticker

    # TODO add in conditional for which radio is selected and then that is assigned to the timeframe variable  

    #  TODO add in conditionals so user fills in correct information into the inputs
    print(f"Ticker: {values['ticker']} Start-Date: {values['start_date']} End-Date: {values['end_date']} Timeframe: {timeframe}")

    if event == sg.WIN_CLOSED:
        break

window.close()