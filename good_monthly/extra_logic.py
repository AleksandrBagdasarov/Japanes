from urllib.parse import urljoin

from parsel import Selector

from .const import *
from core.logger import logger
from core.fetcher import request
import asyncio


class Dict:
    
    @staticmethod
    def get_room_parameters(link: str,price: str, usage_fee: str, initial_cost: str, name: str,
             floor_plan: str, area: str, capacity: str, adress: str, construction_date: str):
        return {
            'link': link,
            'price': price,
            'usage_fee': usage_fee,
            'initial_cost': initial_cost,
            'name': name,
            'floor_plan': floor_plan,
            'area': area,
            'capacity': capacity,
            'adress': adress,
            'construction_date': construction_date,         
        }

    @staticmethod
    def get_name_link_city(tree, xpath):

        name = tree.xpath(f'{xpath}/@alt').extract()
        link = tree.xpath(f'{xpath}/parent::a/parent::li/@id').extract()

        return {n: LINK_TO_LINES.format(l) for n, l in zip(name, link)}
    
    @staticmethod
    def get_name_link(tree, xpath=XPATH_TO_LINES_AND_STATIONS):

        name = tree.xpath(f'{xpath}/text()').extract()
        link = tree.xpath(f'{xpath}/@href').extract()

        return {n.split('(')[0]: urljoin(DOMAIN, l) for n, l in zip(name, link)}


class Rqst:

    @staticmethod
    async def get_cards(station: str) -> list:
        async def reqst(page):

            response = await request("POST", station, headers=HEADERS, data=PAYLOAD_PAGE.format(page))
            if response:

                tree = Selector(response.text)
                urls = tree.xpath("//h3/a/@href").extract()
                for url in urls:
                    links.append(urljoin(DOMAIN, url))
                if urls:
                    page += 1
                    await reqst(page)
        
        links = []
        page = 1        
        await reqst(page)        
        return links

    @staticmethod
    async def get_extract_data(station: str) -> list:
        async def extract_card(link: str) -> list:

            response = await request('GET', link)
            if response:

                tree = Selector(response.text)
                    
                if tree.xpath(XPATH_TO_PRICE_INFO).extract():
                    for month_price, init_cost, usg_fee in [tree.xpath(XPATH_TO_PRICE_LIST).extract()]:
                        price = Text.get_price(Text.get_string(month_price))
                        usage_fee = Text.get_price(Text.get_string(usg_fee))
                        initial_cost = Text.get_price(Text.get_string(init_cost))

                elif tree.xpath(XPATH_TO_PRICE_INFO_2).extract():
                    for month_price, init_cost, usg_fee in [tree.xpath(XPATH_TO_PRICE_LIST_ALTERNATIVE_2).extract()]:
                        price = Text.get_price(Text.get_string(month_price))
                        usage_fee = Text.get_price(Text.get_string(usg_fee))
                        initial_cost = Text.get_price(Text.get_string(init_cost))

                else:
                    for month_price, init_cost, usg_fee in [tree.xpath(XPATH_TO_PRICE_LIST_ALTERNATIVE).extract()]:
                        price = Text.get_price(Text.get_string(month_price))
                        usage_fee = Text.get_price(Text.get_string(usg_fee))
                        initial_cost = Text.get_price(Text.get_string(init_cost))

                name = Text.get_string(tree.xpath("//h2/text()").extract())
                floor_plan = Text.get_string(tree.xpath("//dt[contains(text(), '間取り')]/following-sibling::dd/text()").extract())
                area = Text.extract_area(tree.xpath("//dt[contains(text(), '面積')]/following-sibling::dd/text()").extract_first())
                capacity = Text.get_digits(tree.xpath("//dt[contains(text(), '定員人数')]/following-sibling::dd/text()").extract_first())
                adress = Text.get_string(tree.xpath("//*[contains(text(), '所在地')]/following-sibling::*/text()").extract())
                construction_date = Text.get_date(tree.xpath("//dt[contains(text(), '築年月')]/following-sibling::dd/text()").extract())

                extracted_data.append(Dict.get_room_parameters(link, price, usage_fee, initial_cost, name,
                    floor_plan, area, capacity, adress, construction_date))

        extracted_data = []
        links = await Rqst.get_cards(station)
        if links:
            task = [extract_card(link) for link in links]
            await asyncio.wait(task)

        return extracted_data

class Text:

    @staticmethod
    def get_date(some_list: list) -> str:
        date = Text.get_string(some_list)
        if date:
            return date.replace('年','-').replace('月', '')

    @staticmethod
    def get_string(some_list: list) -> str:
        if some_list:
            return ' '.join([' '.join(x.split()) for x in some_list])

    @staticmethod
    def extract_area(some_str: str) -> str:
        if some_str:
            return ''.join([x for x in some_str if x.isdigit() or x == '.']).replace('²', '')
    
    @staticmethod
    def get_digits(some_str: str) -> str:
        if some_str:
            n = ''.join([x for x in some_str if x.isdigit()])
            if n:
                return int(n)
            else:
                return 0

    @staticmethod
    def get_price(some_str: str) -> list:
        if some_str:
            return max([Text.get_digits(x) for x in some_str.split('/')]) or 0
