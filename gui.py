import PySimpleGUI as sg

title_info = sg.Text("Welcome to StockGraph! Input details below and then a graph will be shown for the stock you are tracking.")

#  ? Get the users input for ticker
ticker = sg.Text("Ticker: ")
ticker_input = sg.InputText(tooltip='Input ticker', key='ticker')

# ? Get the users input for start and end dates in format
start_date = sg.Text("Start date (YYYY-MM-DD): ")
start_date_input = sg.InputText(tooltip='Start Date', key='start_date')
end_date = sg.Text("End date (YYYY-MM-DD): ")
end_date_input = sg.InputText(tooltip='End Date', key='end_date')

# ? Button to link up to a function that gets todays date for the input
end_date_today = sg.Button("Today's Date")

# ? Search button will connect to the function other file and call the API
submit_button = sg.Button("Search")

window = sg.Window('StockGraph', layout=[
    [title_info],
    [ticker, ticker_input],
    [start_date, start_date_input],
    [end_date, end_date_input, end_date_today],
    [submit_button]
])

event, values = window.read()

print(f"Ticker: {values['ticker']} Start-Date: {values['start_date']} End-Date: {values['end_date']}")

window.close()