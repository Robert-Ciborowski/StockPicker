from bs4 import BeautifulSoup
import requests
import pandas as pd
import string


class LinkParser:
    def __init__(self, link):
        self.url = link
        self.parsed = []

    def gather_page_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        ros = soup.find_all('tr', attrs={'class': 'ro'})
        res = soup.find_all('tr', attrs={'class': 're'})
        all_rows = ros + res

        for i in all_rows:
            ticker, name, volume, price, link = self._parse_tr_tag(i)
            # self._parse_tr_tag(i)
            self.parsed.append((ticker, name, volume, price, link))

        return self.parsed

    @staticmethod
    def _parse_tr_tag(tr):
        ticker = tr.find('a').contents[0]
        name = tr.find_all('td')[1].contents[0]
        volume = tr.find_all('td')[5].contents[0].replace(',', '')
        price = tr.find_all('td')[4].contents[0]

        suffix = tr.find('a')['href']
        link = 'https://eoddata.com' + suffix
        # print(ticker)
        # print(name)
        # print(volume)
        # print(price)
        # print(link)

        return ticker, name, volume, price, link


