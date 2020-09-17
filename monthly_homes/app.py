import requests
from parsel import Selector
from urllib.parse import urljoin
import json
from extra_logic import *
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


def extract_station(station: str) -> dict:

    station = Text.extract_station(station)
    # "/hokkaido/chitose_00078-st/list" -> "/chitose_00078-st/"

    req = requests.get(JSON_BY_STATION.format(station))
    response = json.loads(req.text)
    return get_rooms_info(response)




if __name__ == "__main__":
    get_cities()
    # extract_station()
    # get_stations()