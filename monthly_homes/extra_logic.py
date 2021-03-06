from urllib.parse import urljoin

from .const import LINK_TO_CARD
from core.logger import logger

class Dict:

    @staticmethod
    def name_link(tree, xpath):

        return_data = {}

        for line in tree.xpath(f'{xpath}'):
            return_data[line.xpath('./text()').extract_first().strip('ＪＲ')] = line.xpath('./@href').extract_first()

        # name = tree.xpath(f'{xpath}/text()').extract()
        # link = tree.xpath(f'{xpath}/@href').extract()

        # return {n: l for n, l in zip(name, link)}
        return return_data


class Text:

    @staticmethod
    def extract_station(link: str) -> str:
        if link:
            return link.split('/')[2].split('-')[0]


def get_rooms_info(response):
    A = []
    for r in response:
        price = r.get('price_30d')
        initial_cost = r.get('price_30d_initial_cost') - price
        construction_date = r.get('building').get('construction_date')

        A.append(
            dict(
                link = LINK_TO_CARD.format(r.get('id')),
                price = r.get('price_30d'),
                usage_fee = r.get('price_30d'),
                initial_cost = initial_cost,
                name = r.get('name'),
                floor_plan = r.get('floor_plan_text'),
                area = r.get('exclusive_area'),
                capacity = r.get('capacity'),
                adress = r.get('building').get('full_address'),
                construction_date = construction_date[:construction_date.find('-', 5)]
            )
        )

    return A
