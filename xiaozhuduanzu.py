import requests
import json
import time
import pandas as pd
from lxml import etree
from requests.exceptions import RequestException

# print(html.xpath('//*[@id="page_list"]/ul/li/div[2]/div[2]/a/span/text()'))  #标题
# print(html.xpath('//*[@id="page_list"]/ul/li/div[2]/div[1]/span/i/text()'))  #价格
# print(html.xpath('//*[@id="page_list"]/ul/li/@latlng'))#经纬度

def get_one_page(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return etree.HTML(r.text)
        else:
            return None
    except:
        return None


def parse_one_page(html):
    chuzu_title = html.xpath('//*[@id="page_list"]/ul/li/div[2]/div[2]/a/span/text()')
    chuzu_price = html.xpath('//*[@id="page_list"]/ul/li/div[2]/div[1]/span/i/text()')
    chuzu_latlng = html.xpath('//*[@id="page_list"]/ul/li/@latlng')
    for i in range(24):
        chuzu = {}
        chuzu['title'] = chuzu_title[i]
        chuzu['price'] = chuzu_price[i]
        chuzu['latlng'] = chuzu_latlng[i]
        yield chuzu


def write_to_file(content):
    with open('小猪出租.txt','a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(p):
    url = 'https://sz.xiaozhu.com/search-duanzufang-p' + str(p) + '-0/'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(5):
        main(i)
        time.sleep(1)

# 'https://sz.xiaozhu.com/search-duanzufang-p2-0/'
# 'https://sz.xiaozhu.com/search-duanzufang-p3-0/'