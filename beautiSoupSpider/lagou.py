import requests
from bs4 import BeautifulSoup
import pandas
import time
newsary = []

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
for i in range(31):
    time.sleep(2)
    res = requests.get('https://www.lagou.com/zhaopin/Python/'+ str(i) +'?filterOption=3' , headers = headers)
    soup = BeautifulSoup(res.text , 'html.parser') 
    for news in soup.select('.default_list'): #定位
        
        # print(news)
        place = news.find_all(class_ = 'add')[0].text
        companyName = news.select('a')[1].text
        companyClass = news.find_all(class_='industry')[0].text.replace(' ','')
        companySpeak = news.find_all(class_='li_b_r')[0].text
        workName = news.select('h3')[0].text
        workMoney = news.find_all(class_='money')[0].text 
        workNeed = news.find_all(class_='li_b_l')[0].text.split('k')[-1]
        url = news.find_all(class_='position_link')[0]['href']
        newsary.append({'companyName': companyName , 'companyClass' : companyClass , 'companySpeak':companySpeak , 'workName' : workName , 'workMoney' : workMoney , 'workNeed' : workNeed , 'url' : url , 'place' : place})
        
newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('lagou2.xlsx')