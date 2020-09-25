from good_monthly import good_monthly
from monthly_homes import monthly_homes
import asyncio
from core.logger import logger

def get_city_rows() -> dict:
    gm = asyncio.run(good_monthly.get_cities())
    mh = asyncio.run(monthly_homes.get_cities())

    set_of_names = set()
    _id = 0

    for n1, n2 in zip(gm, mh):
        set_of_names.add(n1)
        set_of_names.add(n2)
    data = []

    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))


    return data


def get_lines_rows(city_gm: str, city_mh: str) -> dict:
    gm = asyncio.run(good_monthly.get_lines(city_gm))
    mh = asyncio.run(monthly_homes.get_lines(city_mh))
    # logger.debug(mh)
    set_of_names = set()
    _id = 0
    for n1, n2 in zip(gm, mh):
        set_of_names.add(n1)
        set_of_names.add(n2.strip('ＪＲ'))
    data = {}
    for name in set_of_names:
        data[_id] = dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name))
        _id += 1
    return data


def get_station_rows(station_gm: str, station_mh: str) -> dict:
    gm = asyncio.run(good_monthly.get_stations(station_gm))
    mh = asyncio.run(monthly_homes.get_stations(station_mh))
    logger.debug(mh)
    

# for x,y in get_lines_rows('https://www.good-monthly.com/fukuoka/search/select_line.html', '/fukuoka/').items():
#     print(x,y)
# get_station_rows(, 'hokkaido/chitose-line')

