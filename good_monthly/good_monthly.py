import csv

import requests
from parsel import Selector

from .const import *
from .extra_logic import *
from core.logger import logger


def get_cities() -> list:
    req = requests.get(DOMAIN)
    if req.status_code == 200:
        logger.debug(f'{req.status_code} {DOMAIN}')
        tree = Selector(req.text)
        return Dict.get_name_link_city(tree, XPATH_TO_CITIES)


def get_lines(city: str) -> list:
    # city = 'https://www.good-monthly.com/okinawa/search/select_line.html'
    
    req = requests.get(city)
    if req.status_code == 200:
        tree = Selector(req.text)
        return Dict.get_name_link(tree)


def get_stations(line: str) -> list:
    # line = 'https://www.good-monthly.com/search/select_station.html?rosen_cd=523'
    
    req = requests.get(line)
    if req.status_code == 200:
        tree = Selector(req.text)
        return Dict.get_name_link(tree)



def extract_station(station: str) -> list:
    # station = 'https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758'
    return [Rqst.extract_card(link) for link in Rqst.get_cards(station)]



# if __name__ == "__main__":
#     # for key, value in Rqst.extract_card('https://www.good-monthly.com/detail/?bukken_no=31383').items():
#     #     print(value)
#     # for x in GoodMonthly.get_lines('https://www.good-monthly.com/okinawa/search/select_line.html'):
#     #     print(x)
#     with open('test2.csv', 'w', newline='') as f:
#         fieldnames = ['link','Price per month', 'Usage fee', 'Initial cost', 'Name of listing', 'Floor plan', 'Occupied area (size)', 'Capacity', 'Address', 'Construction date']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()

#         # writer.writerow({'link': 'https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758','Price per month': 0, 'Usage fee': 0, 'Initial cost': 0, 'Name of listing': 0, 'Floor plan': 0, 'Occupied area (size)': 0, 'Capacity': 0, 'Address': 0})
#         for x in GoodMonthly.extract_station('https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758'):
#             writer.writerow(x)
