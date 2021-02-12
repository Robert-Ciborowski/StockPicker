# Name: TSVListingObtainer
# Author: Robert Ciborowski
# Date: 09/02/2021
# Description: Obtains all listings from the TSX Venture Exchange.

# from __future__ import annotations
import csv

import pandas as pd
import urllib.request, json

import requests

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
        self.url = "https://tmxinfoservices.com/files/indices/JX_constituents.csv"

    def obtain(self, addTSVToEndOfTickers=False) -> pd.DataFrame:
        tickers = []

        with requests.Session() as s:
            download = s.get(self.url)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list[4:]:
                if addTSVToEndOfTickers:
                    tickers.append(row[0] + ".TSV")
                else:
                    tickers.append(row[0])

        self.listings = pd.DataFrame({"Ticker": tickers})
        return self.listings
