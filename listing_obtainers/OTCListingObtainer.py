# Name: OTCListingObtainer
# Author: Derek Wang, Robert Ciborowski
# Date: 09/02/2021
# Description: Obtains all OTC listings via webscraping.

# from __future__ import annotations

import pandas as pd
import urllib.request, json

import requests
from bs4 import BeautifulSoup
import string

from listing_obtainers.ListingObtainer import ListingObtainer

class OTCListingObtainer(ListingObtainer):
    amount_to_obtain: int

    def __init__(self, amount_to_obtain=-1):
        super().__init__()
        self.amount_to_obtain = amount_to_obtain
        self.base_url = "https://eoddata.com/stocklist/OTCBB/"

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
