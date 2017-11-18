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
    # print('--------------------------------------------')
    # print(news)
    work_href = ""
    work_name = ""
    try:
        work_href = news.attrs['href']
        work_name = news.text
    except:
        pass
    # print("%s   %s " % (work_href , work_name))
    gongzuo.append({'work_href' : work_href , 'work_name' : work_name})
    # print('--------------------------------------------')
newsdf = pandas.DataFrame(gongzuo)
newsdf.to_excel('gongzuo.xlsx')