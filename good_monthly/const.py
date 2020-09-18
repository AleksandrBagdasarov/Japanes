DOMAIN = 'https://www.good-monthly.com/'
LINK_TO_LINES = 'https://www.good-monthly.com/{}/search/select_line.html'


XPATH_TO_CITIES = "//li/a[@class='open']/img"
XPATH_TO_LINES_AND_STATIONS = "//li/label/a"


PAYLOAD_PAGE = 'disp_count_upper=10&sort=&disp_count_upper=10&priod_time_to_short=&web_yachin_int_ss_to=&web_yachin_int_s_month_to=&web_nyukyo_ninzu=&walk=&good_web_hirosa_from=&good_web_hirosa_to=&chiku_ym=&this_page_no={}&cmd=SELECT_PAGE&disp_count=10&hidden_sort=&random_number=334&hidden_priod_time_to_short=&hidden_web_yachin_int_ss_from=1&hidden_web_yachin_int_ss_to=&hidden_web_yachin_int_s_month_from=1&hidden_web_yachin_int_s_month_to=&hidden_web_nyukyo_ninzu=&hidden_new_web_bed_type1=&hidden_new_web_bed_type2=&hidden_new_web_bed_type3=&hidden_new_web_bed_type4=&hidden_walk=&hidden_good_web_madori_1R=&hidden_good_web_madori_1K=&hidden_good_web_madori_1DK=&hidden_good_web_madori_1LDK=&hidden_good_web_madori_1SLDK=&hidden_good_web_madori_2K=&hidden_good_web_madori_2DK=&hidden_good_web_madori_2LDK=&hidden_good_web_madori_2SLDK=&hidden_good_web_hirosa_from=&hidden_good_web_hirosa_to=&hidden_chiku_ym=&hidden_jyouken_campaign=&hidden_jyouken_guest_house=&hidden_jyouken1=&hidden_setsubi_autoLock=&hidden_setsubi_air_conditioner=&hidden_setsubi_tv=&hidden_setsubi_microwave_oven=&hidden_setsubi_icebox=&hidden_setsubi_closet=&hidden_setsubi_bath_toilet_separate=&hidden_setsubi_washroom_separate=&hidden_setsubi_flooring=&hidden_setsubi_washing_machine=&hidden_setsubi_vacuum_cleaner=&hidden_setsubi_delivery_to_home_box=&hidden_jyouken10=&hidden_hoshounin_flag=&hidden_web_pay3=&hidden_jyouken16=&hidden_setsubi_ih_cooking_heater=&hidden_setsubi_gas_conlo=&hidden_setsubi_addition_heat=&hidden_setsubi_bathroom_dryer=&hidden_setsubi_wash_toilet=&hidden_setsubi_elevator=&hidden_jyouken4=&hidden_jyouken6=&hidden_jyouken17=&hidden_jyouken8=&hidden_telework='
HEADERS = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
  'Origin': 'https://www.good-monthly.com',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8'
}


