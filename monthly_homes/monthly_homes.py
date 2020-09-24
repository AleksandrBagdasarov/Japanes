import csv
import json
from urllib.parse import urljoin

import requests
from parsel import Selector

from .const import *
from .extra_logic import *
from core.logger import logger



def get_cities() -> dict: 
    req = requests.get(DOMAIN)
    if req.status_code == 200:
        logger.debug(f'{req.status_code} {DOMAIN}')
        tree = Selector(req.text)
        return Dict.name_link(tree,XPATH_TO_CITIES)
    # else:
        logger.error(f'{req.status_code}')


def get_lines(city: str) -> dict:
    # city = '/hokkaido/'
    req = requests.get(LINK_TO_LINES.format(city))
    if req.status_code == 200:
        tree = Selector(req.text)
        return Dict.name_link(tree,XPATH_TO_LINES)


def get_stations(line: str) -> dict:
    # line = 'hokkaido/chitose-line'
    req = requests.get(urljoin(DOMAIN, line))

    if req.status_code == 200:
        tree = Selector(req.text)
        return Dict.name_link(tree,XPATH_TO_STATIONS)


def extract_station(station: str) -> list:
    station = Text.extract_station(station)
    # "/hokkaido/chitose_00078-st/list" -> "chitose_00078"

    req = requests.get(JSON_BY_STATION.format(station))
    if req.status_code == 200:
        response = json.loads(req.text)
        return get_rooms_info(response)







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
