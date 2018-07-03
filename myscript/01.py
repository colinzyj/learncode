

import pyquery
import requests


def get_ip_addr(url):
    #ip='114.114.114.114'
    #url='http://ip138.com/ips138.asp?ip=%s&action=2'%ip
    url = url
    rst = requests.get(url)
    query = pyquery.PyQuery(rst.text)
    return query
    #rs = query.find('.ul1 li')[0]
    #return rs
