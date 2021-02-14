from listing_obtainers.TSVListingObtainer import TSVListingObtainer
from stock_filter.StockFilter import StockFilter

obtainer = TSVListingObtainer()
df = obtainer.obtain(addVToEndOfTickers=True)

filter = StockFilter()
filterID = filter.addFilter(["yield"], lambda x: x[0] is not None and x[0] > 0.0)
# print(filter.filter("FD.V"))
results = filter.filterList(df["Ticker"].tolist()[:20])
print(results)
