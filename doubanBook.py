import requests
from bs4 import BeautifulSoup
import pandas

newsary = []

for i in range(10):
    res = requests.get('https://book.douban.com/top250?start=' + str(i*25))
    soup = BeautifulSoup(res.text , 'html.parser') 

    for news in soup.select('.item'): #定位
        person = news.find_all(class_='pl')[1].text.replace(' ','')
        title = news.select('a')[1].text.replace(' ','')

        jianjie = ""
        try:
            jianjie = news.find_all(class_='inq')[0].text 
        except:
            pass;
        
        name = news.select('p')[0].text
        newsary.append({'title': title , 'name': name , 'person':person , 'jianjie': jianjie})

newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('doubanbook1.xlsx')