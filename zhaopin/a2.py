import requests
from bs4 import BeautifulSoup
import csv 
import os
import time
tmp = os.path.exists("lagou2_1.csv")
c = open("lagou2_1.csv", 'a')
writer = csv.writer(c, lineterminator='\n')
if tmp == False:
    writer.writerow(['categoryName','categoryURL'])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

res2 = requests.get("https://www.lagou.com/zhaopin/Java/1", headers = headers)
soup2 = BeautifulSoup(res2.text, 'html.parser')
maxPage = soup2.select('.pager_container')[0].select('a')[4].text
maxPage = 1

for j in range(int(maxPage)):
    print("https://www.lagou.com/zhaopin/Java/" + str(j))
    time.sleep(2)
    res2 = requests.get("https://www.lagou.com/zhaopin/Java/" + str(j+1), headers = headers)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    print(len(soup2.select('.item_con_list li')))
    for news in soup2.select('.item_con_list li'):
        url = news.select('.position_link')[0].attrs['href']
        positionName = news.attrs['data-positionname']
        company = news.attrs['data-company']
        salary = news.attrs['data-salary']
        time = news.select('.format-time')[0].text.strip()
        city = news.select('em')[0].text.strip()
        print([positionName, company, salary, city, time, url])
        break
