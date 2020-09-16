import requests
from parsel import Selector
from urllib.parse import urljoin
import json
from extra_logic import Dict
from contants import *




def get_cities():
    r = requests.get(DOMAIN)
    tree = Selector(r.text)

    cities = tree.xpath(XPATH_TO_CITIES)
    cities_name = cities.xpath('./text()').extract()
    cities_href = cities.xpath('./@href').extract()
    for x, y in zip(cities_name, cities_href):
        print(x, y)
    
    # extract_cards(links)


def extract_cards(station: str):
    
    # station = 'sapporo_00002'
    req = requests.get(JSON_BY_STATION.format(station))
    response = json.loads(req.text)

    for r in response:
        price = r.get('price_30d')
        usage_fee = price / 30
        initial_cost = r.get('price_30d_initial_cost') - price
        name = r.get('name')
        floor_plan = r.get('floor_plan_text')
        area = r.get('exclusive_area')
        capacity = r.get('capacity')
        address = r.get('building').get('full_address')

        A.append(Dict.create(price, usage_fee, initial_cost, name,
                    floor_plan, area, capacity, address))

        get_dicts()


def get_dicts():
    for x in A:
        print('-'*100)
        for y, z in x.items():
            print(y, z)

if __name__ == "__main__":
    # get_cities()
    # extract_cards()