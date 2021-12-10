import requests
from bs4 import BeautifulSoup
import pandas as pd


def item_search():

    # send requests on behalf of a user
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # use csv file to track urls
    product_tracker = pd.read_csv('tracker.csv', sep=',')
    product_tracker_URLs = product_tracker.url


    for item, url in enumerate(product_tracker_URLs):
        # fetch urls
        page = requests.get(url, headers=HEADERS)

        # contains all the info from the url
        soup = BeautifulSoup(page.content, features='lxml')

        # product name
        title = soup.find(id='productTitle').get_text().strip()
        print(title)

        # checking for product price
        price = soup.find('span',{'class': 'a-offscreen'}).get_text().replace(',','').strip()

        # check if item is in stock
        if str('£') in price:
            print(price)

        else:
            print('Item Unavailable')


        print("""   
        """)
    print('End of Search')

item_search()