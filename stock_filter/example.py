from stock_filter.StockFilter import StockFilter

# Returns True. TLSS has 530 employees as of Feb 11, 2021
filter = StockFilter()
filterID = filter.addFilter(["fullTimeEmployees"], lambda x: x[0] < 600)
print(filter.filter("TLSS"))

# Returns False.
filter.removeFilter(filterID)
filterID = filter.addFilter(["fullTimeEmployees"], lambda x: x[0] < 500)
print(filter.filter("TLSS"))
