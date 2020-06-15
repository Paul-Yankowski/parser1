import json

import requests
from bs4 import BeautifulSoup
URL='https://www.mebelshara.ru/contacts'

def get_html(url):
    r=requests.get(url)
    return r
def get_content(html):
 with open('mebel.json', 'w') as f:
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='city-item')
    cities=[]
    for item in items:
        card={
        'address': item.find('h4', class_='js-city-name').text+', '+
         item.find('div', class_='shop-list-item').get('data-shop-address'),
        'latlon': item.find('div', class_='shop-list-item').get('data-shop-latitude')+', '+
         item.find('div', class_='shop-list-item').get('data-shop-longitude'),
        'name': item.find('div', class_='shop-list-item').get('data-shop-name'),
        'working_hours': item.find('div', class_='shop-list-item').get('data-shop-mode1')+', '+
                        item.find('div', class_='shop-list-item').get('data-shop-mode2'),
        'phone': soup.find('span', class_='phone-num').text
        }
        cities.append(card)
    for city in cities:
        json.dump(city,f,ensure_ascii=False)


def parse():
    html = get_html(URL)
    print(html)
    #get_content(html.text)

parse()