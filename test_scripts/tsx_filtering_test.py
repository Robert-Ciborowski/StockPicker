from listing_obtainers.TSXListingObtainer import TSXListingObtainer
from stock_filter.StockFilter import StockFilter

obtainer = TSXListingObtainer()
df = obtainer.obtain(addTOToEndOfTickers=True)

filter = StockFilter()
# This filter will filter based on dividends.
filterFunction = lambda x: x[0] is not None and x[0] > 0.05 or x[1] is not None and x[1] > 0.05
filterID = filter.addFilter(["yield", "dividendYield"], filterFunction)
# print(filter.filter("FD.V"))

# This does the filtering, 100 tickers at a time.
tickerList = df["Ticker"].tolist()

for i in range(0, len(tickerList), 100):
    if i + 100 > len(tickerList):
        end = len(tickerList)
    else:
        end = i + 100
    results, data = filter.filterList(tickerList[i:end])

    for i in range(len(results)):
        print("->", results[i])
        print(data[i])


