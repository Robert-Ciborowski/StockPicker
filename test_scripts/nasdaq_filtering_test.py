from listing_obtainers.NASDAQListingObtainer import NASDAQListingObtainer
from stock_filter.StockFilter import StockFilter

obtainer = NASDAQListingObtainer()
df = obtainer.obtain()

filter = StockFilter()
filterFunction = lambda x: x[0] is not None and x[0] > 0.05 or x[1] is not None and x[1] > 0.05
filterID = filter.addFilter(["yield", "dividendYield"], filterFunction)
# print(filter.filter("FD.V"))
results, data = filter.filterList(df["Ticker"].tolist())

for i in range(len(results)):
    print("->", results[i])
    print(data[i])
