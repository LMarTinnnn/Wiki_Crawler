from urllib import parse
from Wiki_Crawler_Helper.get_links import get_links

pages = set()


def get_all_site(start_url):
    links = get_links(start_url)
    for link in links:
        if link not in pages:
            pages.add(link)
            print(parse.unquote(link))
            get_all_site(link)

get_all_site('')
