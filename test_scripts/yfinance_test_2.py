import yfinance as yf

# msft = yf.Ticker("MSFT")
# print(msft.info)

# Information that we get: {'zip': '98052-6399', 'sector': 'Technology',
# 'fullTimeEmployees': 163000, 'longBusinessSummary': 'Microsoft Corporation
# develops, licenses, and supports software, services, devices, and solutions
# worldwide. Its Productivity and Business Processes segment offers Office,
# Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance,
# and Skype for Business, as well as related Client Access Licenses (CAL);
# Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of
# cloud-based and on-premises business solutions for small and medium
# businesses, large organizations, and divisions of enterprises. Its
# Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio,
# System Center, and related CALs; GitHub that provides a collaboration
# platform and code hosting service for developers; and Azure, a cloud
# platform. It also offers support services and Microsoft consulting services
# to assist customers in developing, deploying, and managing Microsoft server
# and desktop solutions; and training and certification to developers and IT
# professionals on various Microsoft products. Its More Personal Computing
# segment provides Windows original equipment manufacturer (OEM) licensing
# and other non-volume licensing of the Windows operating system; Windows
# Commercial, such as volume licensing of the Windows operating system,
# Windows cloud services, and other Windows commercial offerings; patent
# licensing; Windows Internet of Things; and MSN advertising. It also offers
# Surface, PC accessories, PCs, tablets, gaming and entertainment consoles,
# and other devices; Gaming, including Xbox hardware, and Xbox content and
# services; video games and third-party video game royalties; and Search,
# including Bing and Microsoft advertising. It sells its products through
# OEMs, distributors, and resellers; and directly through digital
# marketplaces, online stores, and retail stores. It has a strategic
# collaboration with DXC Technology. The company was founded in 1975 and is
# headquartered in Redmond, Washington.', 'city': 'Redmond', 'phone':
# '425-882-8080', 'state': 'WA', 'country': 'United States',
# 'companyOfficers': [], 'website': 'http://www.microsoft.com', 'maxAge': 1,
# 'address1': 'One Microsoft Way', 'industry': 'Software—Infrastructure',
# 'previousClose': 242.82, 'regularMarketOpen': 244.78,
# 'twoHundredDayAverage': 216.085, 'trailingAnnualDividendYield':
# 0.008813113, 'payoutRatio': 0.31149998, 'volume24Hr': None,
# 'regularMarketDayHigh': 245.15, 'navPrice': None,
# 'averageDailyVolume10Day': 24712887, 'totalAssets': None,
# 'regularMarketPreviousClose': 242.82, 'fiftyDayAverage': 226.96788,
# 'trailingAnnualDividendRate': 2.14, 'open': 244.78, 'toCurrency': None,
# 'averageVolume10days': 24712887, 'expireDate': None, 'yield': None,
# 'algorithm': None, 'dividendRate': 2.24, 'exDividendDate': 1613520000,
# 'beta': 0.816969, 'circulatingSupply': None, 'startDate': None,
# 'regularMarketDayLow': 242.17, 'priceHint': 2, 'currency': 'USD',
# 'trailingPE': 36.45296, 'regularMarketVolume': 15293599, 'lastMarket':
# None, 'maxSupply': None, 'openInterest': None, 'marketCap': 1843997310976,
# 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume':
# 28445759, 'priceToSalesTrailing12Months': 12.02994, 'dayLow': 242.17,
# 'ask': 244.2, 'ytdReturn': None, 'askSize': 800, 'volume': 15293599,
# 'fiftyTwoWeekHigh': 245.92, 'forwardPE': 30.22126, 'fromCurrency': None,
# 'fiveYearAvgDividendYield': 1.71, 'fiftyTwoWeekLow': 132.52, 'bid': 244.21,
# 'tradeable': False, 'dividendYield': 0.0092, 'bidSize': 800, 'dayHigh':
# 245.15, 'exchange': 'NMS', 'shortName': 'Microsoft Corporation',
# 'longName': 'Microsoft Corporation', 'exchangeTimezoneName':
# 'America/New_York', 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated':
# False, 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY',
# 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market',
# 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 11.627, 'beta3Year':
# None, 'profitMargins': 0.33473998, 'enterpriseToEbitda': 24.861,
# '52WeekChange': 0.32175708, 'morningStarRiskRating': None, 'forwardEps':
# 8.09, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7560500224,
# 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue':
# 17.259, 'sharesShort': 44533174, 'sharesPercentSharesOut': 0.0058999998,
# 'fundFamily': None, 'lastFiscalYearEnd': 1593475200,
# 'heldPercentInstitutions': 0.71844, 'netIncomeToCommon': 51309998080,
# 'trailingEps': 6.707, 'lastDividendValue': 0.56, 'SandP52WeekChange':
# 0.15884686, 'priceToBook': 14.165942, 'heldPercentInsiders': 0.00059,
# 'nextFiscalYearEnd': 1656547200, 'mostRecentQuarter': 1609372800,
# 'shortRatio': 1.39, 'sharesShortPreviousMonthDate': 1609372800,
# 'floatShares': 7431722306, 'enterpriseValue': 1782193848320,
# 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400,
# 'lastSplitFactor': '2:1', 'legalType': None, 'lastDividendDate':
# 1605657600, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth':
# 0.327, 'dateShortInterest': 1611878400, 'pegRatio': 1.82, 'lastCapGain':
# None, 'shortPercentOfFloat': 0.0058999998, 'sharesShortPriorMonth':
# 39201229, 'impliedSharesOutstanding': None, 'category': None,
# 'fiveYearAverageReturn': None, 'regularMarketPrice': 244.78, 'logo_url':
# 'https://logo.clearbit.com/microsoft.com'}

# If you run this, you will stumble onto a bug. You must fix it like so:
# base.py, line 286:
# if len(holders) > 1:
#     self._institutional_holders = holders[1]
# else:
#     self._institutional_holders = ""

# tlss = yf.Ticker("TLSS")
# print(tlss.info)

# Information that we get: {'zip': '33458', 'sector': 'Industrials',
# 'fullTimeEmployees': 530, 'longBusinessSummary': "Transportation and
# Logistics Systems, Inc. provides tractor-trailer and box truck deliveries
# of packages on the east coast of the United States. The company offers
# package delivery services primarily in New York, New Jersey, Pennsylvania,
# Georgia, Florida, Ohio, and Tennessee, principally for Amazon and its
# customers, and for other customers. It also provides various logistics
# services to Amazon and storage solutions for Amazon's customers with
# limited storage facilities. The company is based in Jupiter, Florida.",
# 'city': 'Jupiter', 'phone': '833-764-1443', 'state': 'FL', 'country':
# 'United States', 'companyOfficers': [], 'website':
# 'http://www.tlss-inc.com', 'maxAge': 1, 'address1': '5500 Military Trail',
# 'industry': 'Trucking', 'address2': 'Suite 22-357', 'previousClose':
# 0.06575, 'regularMarketOpen': 0.067, 'twoHundredDayAverage': 0.02539855,
# 'trailingAnnualDividendYield': None, 'payoutRatio': 0, 'volume24Hr': None,
# 'regularMarketDayHigh': 0.0691, 'navPrice': None,
# 'averageDailyVolume10Day': 55577350, 'totalAssets': None,
# 'regularMarketPreviousClose': 0.06575, 'fiftyDayAverage': 0.049606062,
# 'trailingAnnualDividendRate': None, 'open': 0.067, 'toCurrency': None,
# 'averageVolume10days': 55577350, 'expireDate': None, 'yield': None,
# 'algorithm': None, 'dividendRate': None, 'exDividendDate': None, 'beta':
# 4.676025, 'circulatingSupply': None, 'startDate': None,
# 'regularMarketDayLow': 0.06, 'priceHint': 4, 'currency': 'USD',
# 'regularMarketVolume': 31023351, 'lastMarket': None, 'maxSupply': None,
# 'openInterest': None, 'marketCap': 100903152, 'volumeAllCurrencies': None,
# 'strikePrice': None, 'averageVolume': 56809390,
# 'priceToSalesTrailing12Months': 3.0396576, 'dayLow': 0.06, 'ask': 0,
# 'ytdReturn': None, 'askSize': 0, 'volume': 31023351, 'fiftyTwoWeekHigh':
# 3.35, 'forwardPE': None, 'fromCurrency': None, 'fiveYearAvgDividendYield':
# None, 'fiftyTwoWeekLow': 0.01, 'bid': 0, 'tradeable': False,
# 'dividendYield': None, 'bidSize': 0, 'dayHigh': 0.0691, 'exchange': 'PNK',
# 'shortName': 'TRANSPORTATION & LOGISTICS SYS ', 'longName': 'Transportation
# and Logistics Systems, Inc.', 'exchangeTimezoneName': 'America/New_York',
# 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated': False,
# 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY', 'symbol':
# 'TLSS', 'messageBoardId': 'finmb_426560753', 'market': 'us_market',
# 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 3.278, 'beta3Year':
# None, 'profitMargins': -1.2773, 'enterpriseToEbitda': -16.448,
# '52WeekChange': -0.9802985, 'morningStarRiskRating': None, 'forwardEps':
# None, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 1564390016,
# 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue':
# -0.008, 'sharesShort': None, 'sharesPercentSharesOut': None, 'fundFamily':
# None, 'lastFiscalYearEnd': 1577750400, 'heldPercentInstitutions':
# 2.0000001e-05, 'netIncomeToCommon': -61096752, 'trailingEps': -0.171,
# 'lastDividendValue': None, 'SandP52WeekChange': 0.15884686, 'priceToBook':
# None, 'heldPercentInsiders': 0.00411, 'nextFiscalYearEnd': 1640908800,
# 'mostRecentQuarter': 1601424000, 'shortRatio': None,
# 'sharesShortPreviousMonthDate': None, 'floatShares': 1557067013,
# 'enterpriseValue': 108812656, 'threeYearAverageReturn': None,
# 'lastSplitDate': 1531872000, 'lastSplitFactor': '1:250', 'legalType': None,
# 'lastDividendDate': None, 'morningStarOverallRating': None,
# 'earningsQuarterlyGrowth': None, 'dateShortInterest': None, 'pegRatio':
# None, 'lastCapGain': None, 'shortPercentOfFloat': None,
# 'sharesShortPriorMonth': None, 'impliedSharesOutstanding': None,
# 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice':
# 0.067, 'logo_url': 'https://logo.clearbit.com/tlss-inc.com'}

# fdv = yf.Ticker("FD.V")
# print(fdv.info)

# Information that we get: {'zip': 'L4B 1G8', 'sector': 'Technology',
# 'longBusinessSummary': 'Facedrive Inc. operates as a ride-sharing company
# in Canada. It offers Facedrive, a ridesharing platform; and TraceSCAN,
# a COVID-19 contact tracing app. The company was incorporated in 2016 and is
# headquartered in Richmond Hill, Canada.', 'city': 'Richmond Hill', 'state':
# 'ON', 'country': 'Canada', 'companyOfficers': [], 'website':
# 'http://www.facedrive.com', 'maxAge': 1, 'address1': '44 East Beaver
# Creek', 'industry': 'Software—Application', 'address2': 'Suite 16',
# 'previousClose': 47.18, 'regularMarketOpen': 45.99, 'twoHundredDayAverage':
# 17.540218, 'trailingAnnualDividendYield': None, 'payoutRatio': 0,
# 'volume24Hr': None, 'regularMarketDayHigh': 45.99, 'navPrice': None,
# 'averageDailyVolume10Day': 396172, 'totalAssets': None,
# 'regularMarketPreviousClose': 47.18, 'fiftyDayAverage': 25.777647,
# 'trailingAnnualDividendRate': None, 'open': 45.99, 'toCurrency': None,
# 'averageVolume10days': 396172, 'expireDate': None, 'yield': None,
# 'algorithm': None, 'dividendRate': None, 'exDividendDate': None, 'beta':
# None, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow':
# 37.99, 'priceHint': 2, 'currency': 'CAD', 'regularMarketVolume': 398600,
# 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap':
# 3739455744, 'volumeAllCurrencies': None, 'strikePrice': None,
# 'averageVolume': 221069, 'priceToSalesTrailing12Months': 3806.0579,
# 'dayLow': 37.99, 'ask': 39.36, 'ytdReturn': None, 'askSize': None,
# 'volume': 398600, 'fiftyTwoWeekHigh': 60, 'forwardPE': None,
# 'fromCurrency': None, 'fiveYearAvgDividendYield': None, 'fiftyTwoWeekLow':
# 1.96, 'bid': 39.24, 'tradeable': False, 'dividendYield': None, 'bidSize':
# None, 'dayHigh': 45.99, 'exchange': 'VAN', 'shortName': 'FACEDRIVE INC',
# 'longName': 'Facedrive Inc.', 'exchangeTimezoneName': 'America/Toronto',
# 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated': False,
# 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY', 'symbol':
# 'FD.V', 'messageBoardId': 'finmb_608861817', 'market': 'ca_market',
# 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 4502.321,
# 'beta3Year': None, 'profitMargins': 0, 'enterpriseToEbitda': None,
# '52WeekChange': 11.318538, 'morningStarRiskRating': None, 'forwardEps':
# None, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 95248496,
# 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue':
# 0.186, 'sharesShort': 451934, 'sharesPercentSharesOut': 0.0047999998,
# 'fundFamily': None, 'lastFiscalYearEnd': 1577750400,
# 'heldPercentInstitutions': 0.00137, 'netIncomeToCommon': -15904975,
# 'trailingEps': -0.175, 'lastDividendValue': None, 'SandP52WeekChange':
# 0.15884686, 'priceToBook': 211.07526, 'heldPercentInsiders': 0.69977,
# 'nextFiscalYearEnd': 1640908800, 'mostRecentQuarter': 1601424000,
# 'shortRatio': 1.95, 'sharesShortPreviousMonthDate': 1609372800,
# 'floatShares': 27656905, 'enterpriseValue': 4423535104,
# 'threeYearAverageReturn': None, 'lastSplitDate': 1570665600,
# 'lastSplitFactor': '10:1', 'legalType': None, 'lastDividendDate': None,
# 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': None,
# 'dateShortInterest': 1611878400, 'pegRatio': None, 'lastCapGain': None,
# 'shortPercentOfFloat': None, 'sharesShortPriorMonth': 460934,
# 'impliedSharesOutstanding': None, 'category': None,
# 'fiveYearAverageReturn': None, 'regularMarketPrice': 45.99, 'logo_url':
# 'https://logo.clearbit.com/facedrive.com'}



msft = yf.Ticker("MSFT")
info = msft.info

for key, value in info.items():
    print(key, ": ", type(value))

