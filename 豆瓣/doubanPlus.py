import requests
from bs4 import BeautifulSoup
import pandas

newsary = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
for i in range(10):
    res = requests.get('https://movie.douban.com/top250?start='+ str(25*i) +'&filter=' , headers = headers)
    soup = BeautifulSoup(res.text , 'html.parser') 

    for news in soup.select('#content li'): #定位
            
            grade = news.find_all(class_='rating_num')[0].text 
            newsary.append({'author':news.select('p')[0].text , 'grade':grade , 'title':news.select('span')[0].text})
    
newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('douban2.xlsx')


