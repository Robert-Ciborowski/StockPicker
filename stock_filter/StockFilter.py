from typing import List

import yfinance as yf

class StockFilter:
    def __init__(self):
        self.filters = []

    def addFilter(self, valuesToFilter: List, lambdaFilter) -> int:
        """
        Adds a filter. For example, to filter based on # of employees:
        valuesToFilter = ["fullTimeEmployees"]
        lambdaFilter = lambda x: x[0] < 500
        Note that if fullTimeEmployees cannot be found, x = [None]

        :param valuesToFilter: the values to base the filter on
        :param lambdaFilter: the lambda expression
        :return: position of this filter.
        """
        self.filters.append((valuesToFilter, lambdaFilter))
        return len(self.filters) - 1

    def filter(self, ticker: str):
        """
        Filter out this stock. Return the values that the filters
        were given but return None if the stock didn't pass all filters.

        :param ticker: e.g. TLSS
        :return: bool, Dict/None
        """
        yfTicker = yf.Ticker(ticker)
        dataToReturn = {}

        if yfTicker is None:
            print("Could not find info on ticker ", ticker, " from Yahoo!")
            return False, None

        try:
            info = yfTicker.info
        except Exception as e:
            print("Filter got a yahoo finance error when obtaining data for " + ticker + ":")
            print(e)
            return False, None

        for tuple in self.filters:
            valuesToFilter = tuple[0]
            lambdaFilter = tuple[1]
            inputValues = []

            for value in valuesToFilter:
                if value in info:
                    inputValues.append(info[value])
                else:
                    inputValues.append(None)

            returnValue = False

            try:
                returnValue = lambdaFilter(inputValues)
            except:
                print("Got an error when filtering on", ticker, "with inputs",
                      str(inputValues) + ". Assuming the filter returned false.")

            if not returnValue:
                    return False, None

            for i in range(len(valuesToFilter)):
                dataToReturn[valuesToFilter[i]] = inputValues[i]

        return True, dataToReturn

    def filterList(self, tickers: List):
        """
        Runs filters on a list of tickers. Returns tickers that passed the
        filters, as well as their data that was given to the filters.

        :param tickers: e.g. ["TLSS", "TNXP"]
        :return: list of passed tickers, list of Dicts with data
        """
        returnList = []
        dataToReturn = []

        for ticker in tickers:
            print("Filtering", ticker, "...")
            success, data = self.filter(ticker)

            if success:
                returnList.append(ticker)
                dataToReturn.append(data)

        return returnList, dataToReturn

    def removeFilter(self, position: int):
        """
        Removes the filter at position.

        :param position: the position
        """
        if position >= len(self.filters) or position < 0:
            print("removeFilter obtained an invalid position!")

        self.filters.pop(position)



