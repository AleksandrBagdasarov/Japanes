import requests
from constants import *
from parsel import Selector
from extra_logic import *


def get_cities() -> dict: 
    req = requests.get(DOMAIN)

    tree = Selector(req.text)
    return Dict.name_link(tree, XPATH_TO_CITIES)


if __name__ == "__main__":
    print(get_cities())