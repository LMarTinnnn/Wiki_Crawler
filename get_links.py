"""
    get_urls(path)
    # return a list of all valid wiki links in https://zh.wikipedia.org/wiki/{name}

"""
import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup as Bs
from urllib import parse
import random

headers = {
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36'
}
proxies = {
    'http': 'http://12.33.254.195:3128',
    'https': 'http://12.33.254.195:3128'
}


def get_urls(path):
    """

    :param path: /wiki/<词条名称>
    :return: list of all valid wiki links in https://zh.wikipedia.org/wiki/<词条名称>
    """
    urls = set()
    while True:
        try:
            page = requests.get('https://zh.wikipedia.org' + path,
                                headers=headers, timeout=5, proxies=proxies, allow_redirects=False)
        except ProxyError:
            print('代理超时 重试')
        else:
            html = page.text
            soup = Bs(html, 'lxml')
            # print(soup.prettify())
            for url in soup.find(id='bodyContent').findAll('a'):
                href = url.get('href', False)
                if href and href.startswith('/wiki') and ':' not in href:
                    urls.add(href)
            break
    return list(urls)

if __name__ == '__main__':
    quoted_path = parse.quote('/wiki/' + '中国')
    print('Start at: https://zh.wikipedia.org' + parse.unquote(quoted_path))
    links = get_urls(quoted_path)
    while True:
        if not links:
            print('没有链接啦～')
            break
        random_url = random.choice(links)
        print('进入: https://zh.wikipedia.org' + parse.unquote(random_url))
        links = get_urls(random_url)
