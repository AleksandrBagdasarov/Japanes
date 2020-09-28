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


def get_lines_rows(cities: list) -> list:
    def inner(city_gm: str, city_mh: str):
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

    main_data = []
    for city in cities:
        main_data += inner(city.get('good_monthly'), city.get('monthly_homes'))
    
    return main_data



def get_station_rows(lines: list) -> list:
    def inner(line_gm: str, line_mh: str):
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

    main_data = []
    for line in lines:
        main_data += inner(line.get('good_monthly'), line.get('monthly_homes'))
    
    return main_data

    


def get_station_data(stations: list) -> list:
    def inner(station_gm: str, station_mh: str):
        data = []
        if station_gm:
            data += asyncio.run(good_monthly.extract_station(station_gm))
        if station_mh:
            data += asyncio.run(monthly_homes.extract_station(station_mh))

        return data

    main_data = []
    for station in stations:
        main_data += inner(station.get('good_monthly'), station.get('monthly_homes'))
    
    return main_data

# for x in get_station_data([{'good_monthly': 'https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=483|7758', 'monthly_homes':''}]):
#     print(x)

# for x in get_lines_rows('https://www.good-monthly.com/okinawa/search/select_line.html', '/hokkaido/'):
#     print(x)

# for x in get_station_rows([{'good_monthly':'https://www.good-monthly.com/search/select_station.html?rosen_cd=523', 'monthly_homes':'hokkaido/chitose-line'}, {'good_monthly':'https://www.good-monthly.com/search/select_station.html?rosen_cd=523', 'monthly_homes':'hokkaido/chitose-line'}]):
#     print(x)

