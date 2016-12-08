# -*- coding: utf-8 -*-

"""
SoupRefiner
~~~~~~~~~~~~~~~~~~~~~~~~

SoupRefiner is a links parser in Python

~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
    import SoupRefiner
    sr = SoupRefiner(soup_obj)

    internal_links = sr.get_internal_links

    external_links = sr.get_external_links

    """

from urllib import parse

__title__ = 'SoupRefiner'
__author__ = 'LMarTinnnn'


class SoupRefiner(object):
    def __init__(self, soup):
        self.soup = soup
        self.all_links = self.get_links()

    def get_links(self):
        links = set()
        for link in self.soup.findAll('a'):
            href = link.get('href', False)
            if href:
                links.add(href)
        return links

    def get_internal_links(self, include_url):
        """
        :param include_url:  this url determine which url in the page will be [remained].
        :return: return a list of internal links in a web page
        """

        # 获得协议和域名组成的url用于下面的内链检测 和 不完整url的完整化
        p = parse.urlparse(include_url)
        include_url = '%s://%s' % (p.theme, p.netloc)

        internal_links = set()
        all_links = self.soup
        for link in all_links:
            if include_url in link:
                internal_links.add(link)
            elif link.startswith('/'):
                complete_link = include_url + link
                internal_links.add(complete_link)
        return internal_links

    def get_external_links(self, exclude_url):
        """
        :param exclude_url: this url determine which url in the page will be [discarded].
        :return: return a list of external links in a web page
        """
        p = parse.urlparse(exclude_url)
        exclude_url = '%s://%s' % (p.theme, p.netloc)

        external_links = set()
        all_links = self.soup

        for link in all_links:
            # 正则还要好好深入啊 这样实在太麻烦了
            if link.startswith('www') or link.startswith('http') or link.startswith('https'):
                if exclude_url not in link:
                    external_links.add(link)

        return external_links
