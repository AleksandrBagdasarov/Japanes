import requests
from const import *
from parsel import Selector
from extra_logic import *


class GoodMonthly:

    @staticmethod
    def get_cities() -> list: 
        req = requests.get(DOMAIN)

        tree = Selector(req.text)
        return Dict.get_name_link_city(tree, XPATH_TO_CITIES)

    @staticmethod
    def get_lines(city: str) -> list:
        # city = 'hokkaido'
        req = requests.get(city)

        tree = Selector(req.text)
        return Dict.get_name_link(tree)

    @staticmethod
    def get_stations(line: str) -> list:
        # line = 'hokkaido/chitose-line'
        req = requests.get(line)

        tree = Selector(req.text)

        tree = Selector(req.text)
        return Dict.get_name_link(tree)

    # @staticmethod
    # def extract_station(station: str) -> list:
    #     station = Text.extract_station(station)
    #     # "/hokkaido/chitose_00078-st/list" -> "/chitose_00078-st/"

    #     req = requests.get(JSON_BY_STATION.format(station))
    #     response = json.loads(req.text)
    #     return get_rooms_info(response) okinawa


if __name__ == "__main__":
    for x in GoodMonthly.get_stations('https://www.good-monthly.com/search/select_station.html?rosen_cd=523'):
        print(x)    