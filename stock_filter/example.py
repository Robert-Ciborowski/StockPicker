from stock_filter.StockFilter import StockFilter

# Returns True. TLSS has 530 employees as of Feb 11, 2021
filter = StockFilter()
filterID = filter.addFilter(["fullTimeEmployees"], lambda x: x[0] is not None and x[0] < 600)
print(filter.filter("TLSS"))

# Returns False.
filter.removeFilter(filterID)
filterID = filter.addFilter(["fullTimeEmployees"], lambda x: x[0] is not None and x[0] < 500)
print(filter.filter("TLSS"))

# What types of properties can you filter based on?
# zip :  <class 'str'>
# sector :  <class 'str'>
# fullTimeEmployees :  <class 'int'>
# longBusinessSummary :  <class 'str'>
# city :  <class 'str'>
# phone :  <class 'str'>
# state :  <class 'str'>
# country :  <class 'str'>
# companyOfficers :  <class 'list'>
# website :  <class 'str'>
# maxAge :  <class 'int'>
# address1 :  <class 'str'>
# industry :  <class 'str'>
# previousClose :  <class 'float'>
# regularMarketOpen :  <class 'float'>
# twoHundredDayAverage :  <class 'float'>
# trailingAnnualDividendYield :  <class 'float'>
# payoutRatio :  <class 'float'>
# volume24Hr :  <class 'NoneType'>
# regularMarketDayHigh :  <class 'float'>
# navPrice :  <class 'NoneType'>
# averageDailyVolume10Day :  <class 'int'>
# totalAssets :  <class 'NoneType'>
# regularMarketPreviousClose :  <class 'float'>
# fiftyDayAverage :  <class 'float'>
# trailingAnnualDividendRate :  <class 'float'>
# open :  <class 'float'>
# toCurrency :  <class 'NoneType'>
# averageVolume10days :  <class 'int'>
# expireDate :  <class 'NoneType'>
# yield :  <class 'NoneType'>
# algorithm :  <class 'NoneType'>
# dividendRate :  <class 'float'>
# exDividendDate :  <class 'int'>
# beta :  <class 'float'>
# circulatingSupply :  <class 'NoneType'>
# startDate :  <class 'NoneType'>
# regularMarketDayLow :  <class 'float'>
# priceHint :  <class 'int'>
# currency :  <class 'str'>
# trailingPE :  <class 'float'>
# regularMarketVolume :  <class 'int'>
# lastMarket :  <class 'NoneType'>
# maxSupply :  <class 'NoneType'>
# openInterest :  <class 'NoneType'>
# marketCap :  <class 'int'>
# volumeAllCurrencies :  <class 'NoneType'>
# strikePrice :  <class 'NoneType'>
# averageVolume :  <class 'int'>
# priceToSalesTrailing12Months :  <class 'float'>
# dayLow :  <class 'float'>
# ask :  <class 'float'>
# ytdReturn :  <class 'NoneType'>
# askSize :  <class 'int'>
# volume :  <class 'int'>
# fiftyTwoWeekHigh :  <class 'float'>
# forwardPE :  <class 'float'>
# fromCurrency :  <class 'NoneType'>
# fiveYearAvgDividendYield :  <class 'float'>
# fiftyTwoWeekLow :  <class 'float'>
# bid :  <class 'float'>
# tradeable :  <class 'bool'>
# dividendYield :  <class 'float'>
# bidSize :  <class 'int'>
# dayHigh :  <class 'float'>
# exchange :  <class 'str'>
# shortName :  <class 'str'>
# longName :  <class 'str'>
# exchangeTimezoneName :  <class 'str'>
# exchangeTimezoneShortName :  <class 'str'>
# isEsgPopulated :  <class 'bool'>
# gmtOffSetMilliseconds :  <class 'str'>
# quoteType :  <class 'str'>
# symbol :  <class 'str'>
# messageBoardId :  <class 'str'>
# market :  <class 'str'>
# annualHoldingsTurnover :  <class 'NoneType'>
# enterpriseToRevenue :  <class 'float'>
# beta3Year :  <class 'NoneType'>
# profitMargins :  <class 'float'>
# enterpriseToEbitda :  <class 'float'>
# 52WeekChange :  <class 'float'>
# morningStarRiskRating :  <class 'NoneType'>
# forwardEps :  <class 'float'>
# revenueQuarterlyGrowth :  <class 'NoneType'>
# sharesOutstanding :  <class 'int'>
# fundInceptionDate :  <class 'NoneType'>
# annualReportExpenseRatio :  <class 'NoneType'>
# bookValue :  <class 'float'>
# sharesShort :  <class 'int'>
# sharesPercentSharesOut :  <class 'float'>
# fundFamily :  <class 'NoneType'>
# lastFiscalYearEnd :  <class 'int'>
# heldPercentInstitutions :  <class 'float'>
# netIncomeToCommon :  <class 'int'>
# trailingEps :  <class 'float'>
# lastDividendValue :  <class 'float'>
# SandP52WeekChange :  <class 'float'>
# priceToBook :  <class 'float'>
# heldPercentInsiders :  <class 'float'>
# nextFiscalYearEnd :  <class 'int'>
# mostRecentQuarter :  <class 'int'>
# shortRatio :  <class 'float'>
# sharesShortPreviousMonthDate :  <class 'int'>
# floatShares :  <class 'int'>
# enterpriseValue :  <class 'int'>
# threeYearAverageReturn :  <class 'NoneType'>
# lastSplitDate :  <class 'int'>
# lastSplitFactor :  <class 'str'>
# legalType :  <class 'NoneType'>
# lastDividendDate :  <class 'int'>
# morningStarOverallRating :  <class 'NoneType'>
# earningsQuarterlyGrowth :  <class 'float'>
# dateShortInterest :  <class 'int'>
# pegRatio :  <class 'float'>
# lastCapGain :  <class 'NoneType'>
# shortPercentOfFloat :  <class 'float'>
# sharesShortPriorMonth :  <class 'int'>
# impliedSharesOutstanding :  <class 'NoneType'>
# category :  <class 'NoneType'>
# fiveYearAverageReturn :  <class 'NoneType'>
# regularMarketPrice :  <class 'float'>
# logo_url :  <class 'str'>
