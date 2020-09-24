import csv
import json
from urllib.parse import urljoin

import requests
from parsel import Selector

from .const import *
from .extra_logic import *
from core.logger import logger



def get_cities() -> dict: 
    response = requests.get(DOMAIN)
    try:
        assert response.status_code == 200
        
        logger.debug(f'[code:{response.status_code}] {response.url}')

        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_CITIES)

    except AssertionError:
        logger.exception(f'{response.status_code} {response.url}')
    


def get_lines(city: str) -> dict:
    # city = '/hokkaido/'
    response = requests.get(LINK_TO_LINES.format(city))
    try:
        assert response.status_code == 200

        logger.debug(f'[code:{response.status_code}] {response.url}')

        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_LINES)

    except AssertionError:
        logger.exception(f'{response.status_code} {response.url}')


def get_stations(line: str) -> dict:
    # line = 'hokkaido/chitose-line'
    response = requests.get(urljoin(DOMAIN, line))
    try:
        assert response.status_code == 200

        logger.debug(f'[code:{response.status_code}] {response.url}')

        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_STATIONS)

    except AssertionError:
        logger.exception(f'{response.status_code} {response.url}')


def extract_station(station: str) -> list:
    station = Text.extract_station(station)
    # "/hokkaido/chitose_00078-st/list" -> "chitose_00078"

    response = requests.get(JSON_BY_STATION.format(station))
    try:
        assert response.status_code == 200

        logger.debug(f'[code:{response.status_code}] {response.url}')
        
        response = json.loads(response.text)
        return get_rooms_info(response)

    except AssertionError:
        logger.exception(f'{response.status_code} {response.url}')







# if __name__ == "__main__":
#     MonthlyHomes.get_cities()
    # with open('test.csv', 'w', newline='') as f:
    #     fieldnames = ['link','Price per month', 'Usage fee', 'Initial cost', 'Name of listing', 'Floor plan', 'Occupied area (size)', 'Capacity', 'Adress', 'Construction date']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()

    #     stations = '/hokkaido/sapporo_00002-st/list', '/hokkaido/chitose_00078-st/list', '/ishikawa/kanazawa_00186-st/list', '/aichi/nagoya_00005-st/list', '/okinawa/nahakuko_09840-st/list', '/okinawa/miebashi_09847-st/list'
    #     for station in stations:
    #         for x in MonthlyHomes.extract_station(station):
    #             writer.writerow(x)
