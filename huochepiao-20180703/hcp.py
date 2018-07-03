#encoding:utf-8
'''
    火车票查询工具
    modle:requests,docopt,prettytable,colorama

Usage:
    ticket [-dgktz] <from> <to> <date>
    
Options:
    -h --help    显示帮助信息.
    -d           动车.
    -g           高铁
    -k
    -t
    -z
    
'''
import requests
from docopt import docopt
from station import stations

def cli():
    arguments = docopt(__doc__, version='hcp 2.0')
    from_station = stations.get(arguments.get('<from>'),None)
    to_station = stations.get(arguments.get('<to>'),None)
    date = arguments.get('<date>')
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
           'leftTicketDTO.train_date={date}&'
           'leftTicketDTO.from_station={from_station}&'
           'leftTicketDTO.to_station={to_station}&'
           'purpose_codes=ADULT').format(date=date,from_station=from_station,to_station=to_station)
    rsp = requests.get(url)
    raw_trains = rsp.json()['data']['result']
    #return trains
    #print(arguments)
    #return (url)
    print (raw_trains[0])

if __name__ == '__main__':
    cli()
