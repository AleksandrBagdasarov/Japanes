from urllib.parse import urljoin
from const import DOMAIN, XPATH_TO_LINES_AND_STATIONS, LINK_TO_LINES

class Dict:

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
