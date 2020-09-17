import requests
from parsel import Selector
from urllib.parse import urljoin
import json
from extra_logic import Dict
from contants import *




def get_cities() -> dict: 
    req = requests.get(DOMAIN)

    tree = Selector(req.text)
    return Dict.name_link(tree,XPATH_TO_CITIES)


def get_lines(city: str) -> dict:
    # city = '/hokkaido/'
    req = requests.get(LINK_TO_LINES.format(city))

    tree = Selector(req.text)
    return Dict.name_link(tree,XPATH_TO_LINES)



def get_stations(line: str) -> dict:
    # line = 'hokkaido/chitose-line'
    req = requests.get(urljoin(DOMAIN, line))

    tree = Selector(req.text)

    tree = Selector(req.text)
    return Dict.name_link(tree,XPATH_TO_STATIONS)

    # stations_name = tree.xpath(f'{XPATH_TO_STATIONS}/text()').extract()
    # stations_href = tree.xpath(f'{XPATH_TO_STATIONS}/@href').extract()

    # for n, h in zip(stations_name, stations_href):
    #     print(n, h.split('/')[2].split('-')[0])


def extract_station(station: str) -> dict:
    
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
    get_cities()
    # extract_station()
    # get_stations()