import requests
import pandas as pd

# This function gets financials for a company and displays every figure f as
# a ratio of f / revenue
def selectquote(quote):
    r = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/" + quote + "?period=quarter&limit=400&apikey=7385a9af82e189ee7d5e1a3b9297fae3")
    stock = r.json()
    stock = pd.DataFrame.from_dict(stock)
    columnsToDivideByRevenue = stock.columns.tolist()[7:9] + stock.columns.tolist()[10:32]
    # Divide whole dataframe for first row (i.e. revenue)
    # stock[columnsToDivideByRevenue] = stock[columnsToDivideByRevenue].apply(pd.to_numeric, errors='coerce')
    # stock[["revenue"]] = stock[["revenue"]].apply(pd.to_numeric, errors='coerce')
    stock[columnsToDivideByRevenue] = stock[columnsToDivideByRevenue].div(stock.revenue, axis=0)
    return stock

print(selectquote("AAPL"))
