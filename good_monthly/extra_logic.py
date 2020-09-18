from urllib.parse import urljoin
from const import *
import requests
from parsel import Selector
from urllib.parse import urljoin

class Dict:
    
    @staticmethod
    def get_room_parameters(price: str, usage_fee: str, initial_cost: str, name: str,
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
    def get_name_link_city(tree, xpath):

        name = tree.xpath(f'{xpath}/@alt').extract()
        link = tree.xpath(f'{xpath}/parent::a/parent::li/@id').extract()

        return [{'name': n, 'link': LINK_TO_LINES.format(l)} for n, l in zip(name, link)]
    
    @staticmethod
    def get_name_link(tree, xpath=XPATH_TO_LINES_AND_STATIONS):

        name = tree.xpath(f'{xpath}/text()').extract()
        link = tree.xpath(f'{xpath}/@href').extract()

        return [{'name': n, 'link': urljoin(DOMAIN, l)} for n, l in zip(name, link)]


class Rqst:

    @staticmethod
    def get_cards(station: str) -> list:
        # station = 'https://www.good-monthly.com/search/list_eki.html?rosen_eki_cd=523|9236'
        links = []
        page = 1
        def cheker(urls, page):
            if urls:
                page += 1
                reqst(page)

        def reqst(page):
            
            req = requests.request("POST", station, headers=HEADERS, data = PAYLOAD_PAGE.format(page))

            if req.status_code == 200:
                tree = Selector(req.text)
                urls = tree.xpath("//h3/a/@href").extract()

                for url in urls:
                    links.append(urljoin(DOMAIN, url))

            cheker(urls, page)


        reqst(page)
        
        return links

    @staticmethod
    def extract_cards(link: str) -> list:
        req = requests.get(link)
        if req.status_code == 200:
            tree = Selector(req.text)

            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
            name = Text.get_string(tree.xpath("//h2/text()").extract())
            area = Text.extract_area(tree.xpath("//dt[contains(text(), '面積')]/following-sibling::dd/text()").extract_first())
            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
            adress = Text.get_string(tree.xpath("//p[@class='mapLink']/parent::dd/text()").extract())
    

class Text:

    @staticmethod
    def get_string(some_list: list) -> str:
        if some_list:
            return ' '.join([' '.join(x.split()) for x in some_list])

    @staticmethod
    def extract_area(some_str: str) -> str:
        if some_str:
            return some_str.replace('m²', '')
    # def get_digits(some_str: str) -> str:
    #     if some_str:
    #         return ''.join([x for x in some_str if x.isdigit()])
