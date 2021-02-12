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

    def filter(self, ticker: str) -> bool:
        yfTicker = yf.Ticker(ticker)

        if yfTicker is None:
            print("Could not find info on ticker ", ticker, " from Yahoo!")

        info = yfTicker.info

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
                print("Got an error when filtering on ", ticker, " with inputs ",
                      str(inputValues), ". Assuming the filter returned false.")

            if not returnValue:
                return False

        return True

    def removeFilter(self, position: int):
        """
        Removes the filter at position.

        :param position: the position
        """
        if position >= len(self.filters) or position < 0:
            print("removeFilter obtained an invalid position!")

        self.filters.pop(position)



