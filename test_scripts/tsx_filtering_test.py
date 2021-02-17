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
finalResults = []
finalData = []
incrementAmount = 50

for i in range(0, len(tickerList), incrementAmount):
    if i + incrementAmount > len(tickerList):
        end = len(tickerList)
    else:
        end = i + incrementAmount
    results, data = filter.filterList(tickerList[i:end])

    print("Results over the last", incrementAmount, "tickers:")
    for i in range(len(results)):
        print("->", results[i])
        print(data[i])

    finalResults += results
    finalData += data

print("Final results:")
for i in range(len(finalResults)):
    print("->", finalResults[i])
    print(finalData[i])
