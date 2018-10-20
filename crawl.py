# _*_encode=utf-8_*_
from bs4 import BeautifulSoup
import requests
import csv
import time

#抓取杭州信息，可自己修改想要抓取地方的网址
url = 'http://hz.58.com/pinpaigongyu/pn/{page}/'

page = 0

csv_file = open('rent.csv','w')
csv_writer = csv.writer(csv_file,delimiter=',')
#网站对价格进行了加密，用于解密
ss = {'麣':2, '龥':7, '閏':6, '龒':0 , '驋': 4,'鸺': 9,'龤':1,'齤':5,'餼':3,'鑶':8}
while True:
    page += 1
    print('fetch: ',url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text)
    house_list = html.select('.list > li')

    if not house_list:
        break;
    for house in house_list:
        house_title = house.select('h2')[0].string
        house_url = 'http://bj.58.com/%s'%(house.select('a')[0]['href'])
        house_info_list = house_title.split()

        if '公寓' in house_info_list[1] or '青年社区' in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select('.money')[0].select('b')[0].string.strip()
        #解析加密价格数据
        s = ''
        flag = 1
        for i in house_money:
            if i != ' ':
                s += str(ss.get(i))
            elif flag == 1:
                s += '-'
                flag += 1
        print('%s      %s' % (house_title.strip(),s))
        csv_writer.writerow([house_title.strip(),house_location.strip(),s,house_url])
        #睡眠两秒，防止太快ip被屏蔽
        time.sleep(2)
csv_file.close()