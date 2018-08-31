import json

import requests
import time
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
from tweepy import *
import tweepy
from dominate import *


# global variables
trends = []
product_links = []
product_data = []
open(r'C:\AppServ\www\liki\trends.dat', 'w')
open(r'C:\AppServ\www\liki\data.json', 'w')


'''
this function is used to extract trending tweets or handles in a particular geographical area.
this function executes in approximately 2 seconds
'''


def tweet_extraction():
    time_start = time.time()
    config = {}
    exec(open(r'C:\AppServ\www\liki\config.py').read(), config)

    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']
    access_token = config['access_token']
    access_token_secret = config['access_token_secret']

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    trends_place = api.trends_place(23424975)

    for t in trends_place:
        for trending in t['trends']:
            with open('trends.dat', 'a', encoding='utf8') as f:
                f.write("%s\n" % trending['name'].replace('#', ''))
            trends.append("%s" % trending['name'].replace('#', '').replace(' ', '+'))
    print('time taken in extracting trends : ' + str(time.time()-time_start))


'''
this function is used to generate the search result pages and then save those links in flipkart_search_link list
this is done using beautofulsoup module with whos help the links are extracted.
'''


def get_search_url():
    time_start = time.time()
    for trend in trends:
        search_page = requests.get('https://www.flipkart.com/search?q='+trend)
        search_soup = BeautifulSoup(search_page.text, 'html.parser')
        product_link = search_soup.findAll('a', {'class': 'Zhf2z-'})
        if len(product_link) is 0:
            product_link = search_soup.findAll('a', {'class': '_1UoZlX'})
        if len(product_link) > 2:
            for i in range(2):
                product_links.append('http://www.flipkart.com' + product_link[i]['href'].split('&')[0])
    print('time taken in generating urls : ' + str(time.time() - time_start))


def generate_product_details():
    time_start = time.time()
    for linkUrl in product_links:
        product_page = requests.get(linkUrl)
        product_soup = BeautifulSoup(product_page.text, 'html.parser')

        image = product_soup.findAll('img', {'class': 'Yun65Y'})
        if len(image) is 0:
            image = 'null'
        else:
            image = image[0]['src']

        name = product_soup.findAll('h1', {'class': '_35KyD6'})
        if len(name) is 0:
            name = 'null'
        else:
            name = name[0].text

        discount_price = product_soup.findAll('div', {'class': '_1vC4OE'})
        if len(discount_price) is 0:
            discount_price = 'null'
        else:
            discount_price = discount_price[0].text

        original_price = product_soup.findAll('div', {'class': '_3auQ3N'})
        if len(original_price) is 0:
            original_price = 'null'
        else:
            original_price = original_price[0].text

        off = product_soup.findAll('div', {'class': 'VGWI6T'})
        if len(off) is 0:
            off = 'null'
        else:
            off = off[0].text

        product_dic = {
            'image': image,
            'url': linkUrl,
            'name': name,
            'discount_price': discount_price,
            'original_price': original_price,
            'off': off
        }

        product_data.append(product_dic)

        print('time taken in genrating data : ' + str(time.time() - time_start))


if __name__ == "__main__":
    tweet_extraction()
    get_search_url()
    generate_product_details()
    for p in product_data:
        print(p['image'])
        print(p['url'])
        print(p['name'])
        print(p['discount_price'])
        print(p['original_price'])
        print(p['off'])
    f = open(r'C:\AppServ\www\liki\data.json', 'a', encoding='utf8')
    json.dump(product_data, f, indent=4)
