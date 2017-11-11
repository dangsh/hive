import requests
from bs4 import BeautifulSoup
import csv 
import os
tmp3 = os.path.exists("lagou3_1_1.csv")
c3 = open("lagou3_1_1.csv", 'a')
writer3 = csv.writer(c3, lineterminator='\n')
if tmp3 == False:
    writer3.writerow(['categoryName','categoryURL'])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

#最外层 ---> 主页
res = requests.get('https://www.lagou.com/jobs/1939134.html', headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.container-body .dn dl'):
    mainCategoryName = news.select('dt')[0].text.strip()
    for i, item in enumerate(news.select('a')):
        try:
            categoryName = item.text.strip()
            categoryURL = item.attrs['href']
            writer3.writerow([mainCategoryName, categoryName, categoryURL])
        except Exception as e:
            raise e