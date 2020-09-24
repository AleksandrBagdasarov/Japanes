from good_monthly import good_monthly
from monthly_homes import monthly_homes
import asyncio


def get_city_rows():
    gm = good_monthly.get_cities()
    mh = monthly_homes.get_cities()
    set_of_names = set()
    _id = 0
    for n1, n2 in zip(gm, mh):
        set_of_names.add(n1)
        set_of_names.add(n2)
    data = {}
    for name in set_of_names:
        data[_id] = dict(name=name, good_monthly=gm.get(name), monthly_homes=mh.get(name))
        _id += 1
    return data


def get_lines_rows(id:int):

    pass

async def test():
    for x, y in await get_city_rows().items():
        print(y.get('good_monthly'))
        print(y.get('monthly_homes'))
        print(asyncio.run(good_monthly.get_lines(y.get('good_monthly'))))
        print(asyncio.run(monthly_homes.get_lines(y.get('monthly_homes'))))


asyncio.run(test())