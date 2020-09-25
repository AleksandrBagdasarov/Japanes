from good_monthly import good_monthly
from monthly_homes import monthly_homes
import asyncio
from core.logger import logger

def get_city_rows() -> list:
    set_of_names = set()

    gm = asyncio.run(good_monthly.get_cities())
    if gm:
        for name in gm:
            set_of_names.add(name)
    else:
        gm = {}
    
    mh = asyncio.run(monthly_homes.get_cities())
    if mh:
        for name in mh:
            set_of_names.add(name)
    else:
        mh = {}

    data = []
    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))

    return data


def get_lines_rows(city_gm: str, city_mh: str) -> list:
    set_of_names = set()
    gm = {}
    mh = {}

    if city_gm:
        gm = asyncio.run(good_monthly.get_lines(city_gm))
        for name in gm:
            set_of_names.add(name)

    if city_mh:
        mh = asyncio.run(monthly_homes.get_lines(city_mh))
        for name in mh:
            set_of_names.add(name.strip('ＪＲ'))

    data = []
    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))

    return data


def get_station_rows(line_gm: str, line_mh: str) -> list:
    set_of_names = set()
    gm = {}
    mh = {}

    if line_gm:
        gm = asyncio.run(good_monthly.get_stations(line_gm))
        for name in gm:
            set_of_names.add(name)

    if line_mh:
        mh = asyncio.run(monthly_homes.get_stations(line_mh))
        for name in mh:
            set_of_names.add(name)
    
    data = []
    for name in set_of_names:
        data.append(dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name)))

    return data


def get_station_data(station_gm: str, station_mh: str) -> list:
    data = []
    if station_gm:
        data += asyncio.run(good_monthly.extract_station(station_gm))
    if station_mh:
        data += asyncio.run(monthly_homes.extract_station(station_mh))

    return data


# get_station_data('https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758', '')

# for x in get_lines_rows('https://www.good-monthly.com/okinawa/search/select_line.html', '/hokkaido/'):
#     print(x)
# get_station_rows('https://www.good-monthly.com/search/select_station.html?rosen_cd=523', 'hokkaido/chitose-line')

# for x in get_city_rows():
#     print(x)

# print(get_city_rows())