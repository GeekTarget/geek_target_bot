import base64
import requests
from bs4 import BeautifulSoup

Id = '402480'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_ym_d=1598363041; _ym_uid=1598363041163280418; _ym_visorc_44060479=b; _ym_isad=2; _ym_visorc_26812653=b',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}


def write_id(filename, id):
    with open(filename, 'w') as file:
        file.write(id)


def get_file_id(filename):
    f = open(filename).read()
    return f


def decrypt_url(data: str, key: str) -> str:
    """ Расшифровывает защищённую ссылку """
    if data.startswith('#'):
        data = data[1:]

    for x in key[::-1]:
        data = x.join(reversed(data.split(x)))

    return base64.b64decode(data).decode('utf-8')


def get_main():
    global r
    r = requests.get('https://ru.sefon.cc/news/',headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    new_music = soup.find('div', class_="b_list_mp3s _").find('div', class_='mp3')
    return new_music

def get_content():
    music = get_main()
    root = BeautifulSoup(r.content, 'html.parser')
    data = root.select('.url_protected')[0]['data-url']
    key = root.select('.url_protected')[0]['data-key']
    url = decrypt_url(data, key)
    text = {
        'artist_name': music.find('div', class_="artist_name").get_text(),
        'music_name': music.find('div', class_='song_name').get_text(strip=True),
        'url': url
    }
    new_music = 'Новый трек!' + '\n' + text['artist_name'] + ' - ' + text['music_name'] + '\n' + 'Слушать → ' + text[
        'url']
    return new_music


def get_id():
    music = get_main()
    id = music.get('data-mp3_id')
    return id
