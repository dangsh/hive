# rank-view-list li
import requests
from bs4 import BeautifulSoup
import pandas

newsary = []


for i in range(25):
    res = requests.get('http://r.qidian.com/yuepiao?chn=-1&page='+str(i))
    soup = BeautifulSoup(res.text , 'html.parser') 

    for news in soup.select('.rank-view-list li'): #定位
        # print(news)

        # print(news.select('a')[1].text,news.select('a')[2].text,news.select('a')[3].text,news.select('p')[1].text,news.select('p')[2].text,news.select('a')[0]['href'])

        newsary.append({'title':news.select('a')[1].text,'name':news.select('a')[2].text,'style':news.select('a')[3].text,'describe':news.select('p')[1].text,'lastest':news.select('p')[2].text,'url':news.select('a')[0]['href']})


newsdf = pandas.DataFrame(newsary)
# print(newsdf)
newsdf.to_excel('qidian2.xlsx')
# newsdf.to_excel('qidian_rank1.xlsx')