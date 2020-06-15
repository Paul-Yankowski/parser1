import json

import requests
from bs4 import BeautifulSoup
URL='https://www.mebelshara.ru/contacts'

def get_html(url):
    response=requests.get(url)
    return response
def get_content(html):
 with open('mebel.json', 'w') as f:
    soup = BeautifulSoup(html,'html.parser')
    shops = soup.find_all('div', class_='city-item')
    parsed_shops=[]
    for shop in shops:
        parsed_shop={
        'address': shop.find('h4', class_='js-city-name').text+', '+
         shop.find('div', class_='shop-list-item').get('data-shop-address'),
        'latlon': shop.find('div', class_='shop-list-item').get('data-shop-latitude')+', '+
         shop.find('div', class_='shop-list-item').get('data-shop-longitude'),
        'name': shop.find('div', class_='shop-list-item').get('data-shop-name'),
        'working_hours': shop.find('div', class_='shop-list-item').get('data-shop-mode1')+', '+
                        shop.find('div', class_='shop-list-item').get('data-shop-mode2'),
        'phone': soup.find('span', class_='phone-num').text
        }
        parsed_shops.append(parsed_shop)
    for parsed_shop in parsed_shops:
        json.dump(parsed_shop,f,ensure_ascii=False)


def parse():
    html = get_html(URL)
    get_content(html.text)

parse()