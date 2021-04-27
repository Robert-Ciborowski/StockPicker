# Name: TSVListingObtainer
# Author: Robert Ciborowski
# Date: 09/02/2021
# Description: Obtains all listings from the TSX Venture Exchange.
# derek do this 8==D
# from __future__ import annotations
import csv

import pandas as pd
import urllib.request, json

import requests
from bs4 import BeautifulSoup
import string

from listing_obtainers.ListingObtainer import ListingObtainer

# THIS IS NOT FINISHED! It only gets the Venture Composite Index (^JX) stocks.
# We need a better data source.

class TSVListingObtainer(ListingObtainer):
    amount_to_obtain: int

    """
    If amount_to_obtain is negative, then all listings will be obtained.
    You can just not pass it in since it's optional.
    """
    def __init__(self, amount_to_obtain=-1):
        super().__init__()
        self.amount_to_obtain = amount_to_obtain
        # self.url = "https://tmxinfoservices.com/files/indices/JX_constituents.csv"
        self.base_url = "http://eoddata.com/stocklist/TSXV/"

    # def obtain(self, addVToEndOfTickers=False) -> pd.DataFrame:
    #     tickers = []
    #
    #     with requests.Session() as s:
    #         download = s.get(self.url)
    #         decoded_content = download.content.decode('utf-8')
    #
    #         cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    #         my_list = list(cr)
    #         for row in my_list[5:]:
    #             if addVToEndOfTickers:
    #                 tickers.append(row[1] + ".V")
    #             else:
    #                 tickers.append(row[1])
    #
    #     self.listings = pd.DataFrame({"Ticker": tickers})
    #     return self.listings

    def obtain(self) -> pd.DataFrame:
        tickers = []
        alphabet_string = string.ascii_uppercase
        alphabet_list = list(alphabet_string)

        for i in alphabet_list:
            url = self.base_url + i + ".htm"
            tickers += self._gather_data(url)

        self.listings = pd.DataFrame({"Ticker": tickers})
        return self.listings

    def _gather_data(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        ros = soup.find_all('tr', attrs={'class': 'ro'})
        res = soup.find_all('tr', attrs={'class': 're'})
        all_rows = ros + res
        tickers = []

        for i in all_rows:
            ticker = self._parse_tr_tag(i)
            tickers.append(ticker)

        return tickers

    def _parse_tr_tag(self, tr):
        # Put more stuff here if we want to add more things to the returned
        # DataFrame in obtain(). See Derek's Test Code/webscrape.py for more.
        ticker = tr.find('a').contents[0]
        return ticker

