import webscrape
import string


def main():

    base_url = 'https://eoddata.com/stocklist/OTCBB/'

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    data_set = {}

    for i in alphabet_list:
        url = base_url + i + '.htm'
        page = webscrape.LinkParser(url)
        data_set[i] = page.gather_page_data()

    return data_set


if __name__ == "__main__":
    print(main())
