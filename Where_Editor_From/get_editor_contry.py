from Wiki_Crawler_Helper.get_links import get_links
from config.config import headers
import config.config
import requests
from urllib import parse
from bs4 import BeautifulSoup
import re
import random
# from get_country import get_country
from google_get_country import get_country
# Counter 是 dict 的 子类 用来统计重复出现的个数
from collections import Counter


def get_history_ips(wiki_name, proxies):
    # 这个页面会限制ip访问次数
    history_url = 'http://vs.aka-online.de/cgi-bin/wppagehiststat.pl?lang=zh.wikipedia&page=' + wiki_name
    res = requests.get(history_url, headers=headers, timeout=3, proxies=proxies)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    ip_addresses = set()
    for ip in soup.findAll('a', string=re.compile(r'\d{1,3}(\.\d{1,3}){3}')):
        ip_addresses.add(ip.string)
    return ip_addresses


def main():
    # 从首页开始随机爬
    # 广度优先
    links = get_links('')
    seen = set()
    c = Counter()
    seen.add('')
    while len(links) > 0:
        # 给历史修改者函数送一个代理
        proxy = config.config.proxies
        for link in links:
            if link in seen:
                continue
            seen.add(link)
            name = parse.unquote(link.strip('/wiki/'))
            print('\n---------------------- Start Counter at [%s] ----------------------' % name)
            ips = get_history_ips(name, proxy)
            if not ips:
                print('此页面没有匿名修改\n')
            else:
                for ip in ips:
                    country = get_country(ip)
                    if not country:
                        continue
                    c[country] += 1
                    print('修改来自:' + ip + ' 归属: ' + country)
            print('当前统计状况')
            print(c)
        links = get_links(random.choice(links))


if __name__ == '__main__':
    main()