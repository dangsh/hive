import os
import requests
from bs4 import BeautifulSoup
import csv
tmp = os.path.exists("500.csv")
c = open("500.csv","a")
writer = csv.writer(c, lineterminator='\n')
if tmp == False:
    writer.writerow(['title', 'name', 'style', 'describe', 'lastest', 'url'])
for i in range(1):
    res = requests.get('http://r.qidian.com/yuepiao?chn=-1&page='+str(i))
    soup = BeautifulSoup(res.text , 'html.parser') 
    for news in soup.select('.rank-view-list li'): #定位
        data = []
        data.append(news.select('a')[1].text.strip())
        data.append(news.select('a')[2].text.strip())
        data.append(news.select('a')[3].text.strip())
        data.append(news.select('p')[1].text.strip())
        data.append(news.select('p')[2].text.strip())
        data.append(news.select('a')[0]['href'].strip())
        writer.writerow(data)