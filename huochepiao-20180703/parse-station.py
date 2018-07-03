#encoding:utf-8
import requests,re
from pprint import pprint


def main():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
    rsp=requests.get(url)
    pattern=u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = re.findall(pattern,rsp.text)
    pprint (dict(result),indent=4)

    #print(rsp.text)

if __name__=='__main__':
    main()
