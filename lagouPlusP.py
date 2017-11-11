import requests
from bs4 import BeautifulSoup
import pandas
import time

newsary = []
gongzuo = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
res = requests.get('https://www.lagou.com/' , headers = headers)
soup = BeautifulSoup(res.text , 'html.parser') 
for news in soup.select('#sidebar a'): #定位
    work_href = ""
    work_name = ""
    try:
        work_href = news.attrs['href']
        work_name = news.text
    except:
        pass
    gongzuo.append(work_href)


gongzuo = gongzuo[:3]

for j in gongzuo:
    print(j)
    for i in range(2):
        # time.sleep(2)
        res = requests.get( j + str(i+1) , headers = headers)
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
newsdf.to_excel('lagouPlusp.xlsx')



# print(gongzuo)