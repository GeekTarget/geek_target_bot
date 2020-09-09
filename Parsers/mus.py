from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
import os

global Status
Status = 0

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options)

HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'yuidss=4186114581598362833; yandexuid=4186114581598362833; i=KW5dcM5et8jwem7/STiBGhSxKFG5/UEREvT/QrJ5R326setiqpNXCSw92Bu48wi1u3ZvDKp+KK5zY77XI/Vr/InmAO4=; ymex=1913722836.yrts.1598362836#1913722835.yrtsi.1598362835; mda=0; zm=m-white_bender_zen-ssr.webp.css-https%3As3home-static_PvIkGO3Vcytb9M-iI15qeAiR580%3Al; _ym_uid=1598773133972937467; yc=1599032333.zen.cacS%3A1598776762; cycada=XOTqSvIYXq1/Jj8lvwK6whf4iDbQ8owzGe5smz/tY+M=; yandex_gid=44; my=YysBLAA=; _ym_d=1598773975; skid=9160909461598774034; yp=1630310006.ygu.0#1614541167.szm.1_25:1536x864:1536x702#1630309287.p_sw.1598773287#1598859783.ln_tp.01#1598860297.nps.7637147971%3Aclose#1630310006.ygo.40%3A44; yabs-frequency=/5/100802LUIrz6NKjV/VbMmS9K0003OF43xLB1mbG000DWyG1UCSd2K0000sJoX0G00/; pepsi_year=today; device_id="bbcfc7cbc97d861ffcb90ff51f78f137b945e4897"; _ym_wasSynced=%7B%22time%22%3A1599497702228%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; gdpr=0; _ym_isad=2; _ym_visorc_26812653=b; _ym_visorc_1028356=b; active-browser-timestamp=1599503863279',
'Host': 'music.yandex.ru',
'Referer': 'https://www.google.com/',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

def get_main():
    driver.get('https://music.yandex.ru/new-releases')
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    music = soup.find('div',class_='album album_selectable')
    return music


def get_content():
    music = get_main()
    url = music.find('div',class_='album__title deco-typo typo-main').find('a',class_="d-link deco-link album__caption").get('href')
    protocol = 'https://music.yandex.ru'
    return protocol + url


def get_status():
    music = get_main()
    status = music.find('div',class_='album__title deco-typo typo-main').get('title')
    return status

