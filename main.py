from good_monthly import good_monthly
from monthly_homes import monthly_homes
import asyncio
from core.logger import logger

def get_city_rows() -> dict:
    gm = asyncio.run(good_monthly.get_cities())
    mh = asyncio.run(monthly_homes.get_cities())

    set_of_names = set()
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
    
    set_of_names = set()
    for n1, n2 in zip(gm, mh):
        set_of_names.add(n1)
        set_of_names.add(n2.strip('ＪＲ'))

    data = []
    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))

    return data


def get_station_rows(line_gm: str, line_mh: str) -> dict:
    gm = asyncio.run(good_monthly.get_stations(line_gm))
    mh = asyncio.run(monthly_homes.get_stations(line_mh))

    set_of_names = set()
    for n1, n2 in zip(gm, mh):
        set_of_names.add(n1)
        set_of_names.add(n2)
    
    data = []
    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))

    return data


def get_station_data(station_gm: str, station_mh: str) -> dict:
    gm = asyncio.run(good_monthly.extract_station(station_gm))
    mh = asyncio.run(monthly_homes.extract_station(station_mh))
    
    data = gm + mh
    for row in data:
        print(row)
    return data


get_station_data('https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758', "/hokkaido/chitose_00078-st/list")
# for x in get_station_rows('https://www.good-monthly.com/search/select_station.html?rosen_cd=523', 'hokkaido/chitose-line'):
#     print(x)
# get_station_rows('https://www.good-monthly.com/search/select_station.html?rosen_cd=523', 'hokkaido/chitose-line')

