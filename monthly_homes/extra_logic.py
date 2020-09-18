from urllib.parse import urljoin

from const import LINK_TO_CARD


class Dict:

    @staticmethod
    def get_room_parameters(link: str, price: str, usage_fee: str, initial_cost: str, name: str,
             floor_plan: str, area: str, capacity: str, adress: str):
        return {
            'link': link,
            'Price per month': price,
            'Usage fee': usage_fee,
            'Initial cost': initial_cost,
            'Name of listing': name,
            'Floor plan': floor_plan,
            'Occupied area (size)': area,
            'Capacity': capacity,
            'Adress': adress,            
        }

    @staticmethod
    def name_link(tree, xpath):

        name = tree.xpath(f'{xpath}/text()').extract()
        link = tree.xpath(f'{xpath}/@href').extract()

        return [{'name': n, 'link': l} for n, l in zip(name, link)]


class Text:

    @staticmethod
    def extract_station(link: str) -> str:
        return link.split('/')[2].split('-')[0]


def get_rooms_info(response):
    A = []
    for r in response:
        link = LINK_TO_CARD.format(r.get('id'))
        price = r.get('price_30d')
        usage_fee = r.get('price_30d')
        initial_cost = r.get('price_30d_initial_cost') - price
        name = r.get('name')
        floor_plan = r.get('floor_plan_text')
        area = r.get('exclusive_area')
        capacity = r.get('capacity')
        adress = r.get('building').get('full_address')

        A.append(Dict.get_room_parameters(link, price, usage_fee, initial_cost, name,
                    floor_plan, area, capacity, adress))

    return A
