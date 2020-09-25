import csv
import json
from urllib.parse import urljoin

# import requests
from parsel import Selector

from .const import *
from .extra_logic import *
from core.logger import logger
from core.fetcher import request


async def get_cities() -> dict: 
    response = await request('GET', DOMAIN)
    if response:
        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_CITIES)
    


async def get_lines(city: str) -> dict:
    # city = '/hokkaido/'
    logger.debug(f'expected: "/hokkaido/" got: {city}')
    response = await request('GET', LINK_TO_LINES.format(city))
    if response:
        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_LINES)


async def get_stations(line: str) -> dict:
    # line = 'hokkaido/chitose-line'
    logger.debug(f'expected: "hokkaido/chitose-line" got: {line}')
    response = await request('GET', urljoin(DOMAIN, line))
    if response:
        tree = Selector(response.text)
        return Dict.name_link(tree,XPATH_TO_STATIONS)


async def extract_station(station: str) -> list:
    # station = "/hokkaido/chitose_00078-st/list"
    logger.debug(f'expected: "/hokkaido/chitose_00078-st/list" got: {station}')
    response = await request('GET', JSON_BY_STATION.format(Text.extract_station(station)))
    if response:
        return get_rooms_info(json.loads(response.text))







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
