from urllib import parse
import requests
from config.config import headers


def get_country(ip_or_hostname):
    """

    :param ip_or_hostname: ip address you wanna check or netloc of a url
    :return: a tuple like (country_code, country_name)
    """
    base_url = 'http://freegeoip.net/json/'
    # !!!!!! 下面这行必须加括号！ 不然逻辑会变成 if ('http') or ('https' in ip_or_hostname) 永远是True
    if ('http' or 'https') in ip_or_hostname:
        ip_or_hostname = parse.urlparse(ip_or_hostname).netloc
    query_url = base_url + str(ip_or_hostname)
    try:
        data = requests.get(query_url, headers=headers, timeout=3).json()
        # country_code = data['country_code']
        country_name = data['country_name']
        return country_name
    except:
        return '未知'

if __name__ == '__main__':
    print(get_country('47.88.188.254'))