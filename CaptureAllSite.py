from get_links import get_urls
from urllib import parse
from requests.exceptions import ProxyError


pages = set()


def get_all_site(start_url):
    links = get_urls(start_url)
    for link in links:
        if link not in pages:
            pages.add(link)
            print(parse.unquote(link))
            get_all_site(link)

get_all_site('')
