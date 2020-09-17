

class Dict:

    @staticmethod
    def create(price: str, usage_fee: str, initial_cost: str, name: str,
             floor_plan: str, area: str, capacity: str, address: str):
        return {
            'Price per month': price,
            'Usage fee': usage_fee,
            'Initial cost': initial_cost,
            'Name of listing': name,
            'Floor plan': floor_plan,
            'Occupied area (size)': area,
            'Capacity': capacity,
            'Address': address,            
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