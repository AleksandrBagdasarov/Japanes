from constants import LINK_TO_LINES

class Dict:

    @staticmethod
    def name_link(tree, xpath):

        name = tree.xpath(f'{xpath}/@alt').extract()
        link = tree.xpath(f'{xpath}/parent::a/parent::li/@id').extract()

        return [{'name': n, 'link': LINK_TO_LINES.format(l)} for n, l in zip(name, link)]