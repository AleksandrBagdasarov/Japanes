import requests
from parsel import Selector
from urllib.parse import urljoin
import json
from extra_logic import *
from contants import *

import csv

class MonthlyHomes:

    @staticmethod
    def get_cities() -> dict: 
        req = requests.get(DOMAIN)
        if req.status_code == 200:
            tree = Selector(req.text)
            return Dict.name_link(tree,XPATH_TO_CITIES)

    @staticmethod
    def get_lines(city: str) -> dict:
        # city = '/hokkaido/'
        req = requests.get(LINK_TO_LINES.format(city))
        if req.status_code == 200:
            tree = Selector(req.text)
            return Dict.name_link(tree,XPATH_TO_LINES)

    @staticmethod
    def get_stations(line: str) -> dict:
        # line = 'hokkaido/chitose-line'
        req = requests.get(urljoin(DOMAIN, line))

        if req.status_code == 200:
            tree = Selector(req.text)
            return Dict.name_link(tree,XPATH_TO_STATIONS)

    @staticmethod
    def extract_station(station: str) -> list:
        station = Text.extract_station(station)
        # "/hokkaido/chitose_00078-st/list" -> "/chitose_00078-st/"

        req = requests.get(JSON_BY_STATION.format(station))
        if req.status_code == 200:
            response = json.loads(req.text)
            return get_rooms_info(response)




STATIONS = '/hokkaido/sapporo_00002-st/list', '/hokkaido/chitose_00078-st/list', '/ishikawa/kanazawa_00186-st/list', '/aichi/nagoya_00005-st/list', '/okinawa/nahakuko_09840-st/list', '/okinawa/miebashi_09847-st/list'


if __name__ == "__main__":
    with open('test.csv', 'w', newline='') as f:
        fieldnames = ['link','Price per month', 'Usage fee', 'Initial cost', 'Name of listing', 'Floor plan', 'Occupied area (size)', 'Capacity', 'Address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


        for station in STATIONS:
            writer.writerow({'link': urljoin(DOMAIN, station),'Price per month': 0, 'Usage fee': 0, 'Initial cost': 0, 'Name of listing': 0, 'Floor plan': 0, 'Occupied area (size)': 0, 'Capacity': 0, 'Address': 0})
            for x in MonthlyHomes.extract_station(station):
                writer.writerow(x)


                print(x)
                print('-- -- ' * 10)
