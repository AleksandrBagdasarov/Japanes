DOMAIN = 'https://monthly.homes.jp/'
LINK_TO_LINES = 'https://monthly.homes.jp{}line'
JSON_BY_STATION = 'https://monthly-api.vacation-stay.jp/v2/room_types?per=20&station={}'

XPATH_TO_CITIES = "//li[@class='p-areaPrefGroup__item']//a"
XPATH_TO_LINES = "//li[@class='c-lineCheckGroup__item--quarter']//a"
XPATH_TO_STATIONS = "//li[@class='c-lineCheckGroup__item']//a"

A = []

CITIES = {
    '北海道': '/hokkaido/',
    '青森': '/aomori/',
    '岩手': '',
    '宮城': '/miyagi/'
}

STATIONS = {
    '旭川': 'asahikawa_00085',
    '麻生': 'asabu_06551',
    '岡山': 'okayama_00029'
}

