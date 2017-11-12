import requests
from bs4 import BeautifulSoup
import pandas

newsary = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# res = requests.get('https://movie.douban.com/top250' , headers = headers)
for i in range(10):
    res = requests.get('https://movie.douban.com/top250?start='+ str(25*i) +'&filter=' , headers = headers)
    soup = BeautifulSoup(res.text , 'html.parser') 
    for news in soup.select('#content li'): #定位
            newsary.append({'title':news.select('span')[0].text , 'author':news.select('p')[0].text})
newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('douban.xlsx')



# https://movie.douban.com/top250?start=0&filter=
# https://movie.douban.com/top250?start=25&filter=
# https://movie.douban.com/top250?start=50&filter=