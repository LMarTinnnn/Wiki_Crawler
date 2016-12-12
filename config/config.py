from ProxyFinder.Ip_pool_foreign import IpPool
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36'
}

ips = IpPool('http://vs.aka-online.de/cgi-bin/wppagehiststat.pl', ip_number=5, foreign=True).give_me_ip()
wiki_ips = IpPool('https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5', ip_number=5, foreign=False).give_me_ip()

wiki_ip = random.choice(wiki_ips)
wiki_proxy = {
    'http': wiki_ip,
    'https': wiki_ip
}

ip = random.choice(ips)
proxies = {
    'http': ip,
    'https': ip
}