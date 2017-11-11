import requests
from bs4 import BeautifulSoup
import csv 
import os
tmp = os.path.exists("lagou.csv")
c = open("lagou.csv", 'a')
writer = csv.writer(c, lineterminator='\n')
if tmp == False:
    writer.writerow(['categoryName','categoryURL'])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

#最外层 ---> 主页
res = requests.get('https://www.lagou.com/', headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.container-body .dn dl'):
    mainCategoryName = news.select('dt')[0].text.strip()
    for i, item in enumerate(news.select('a')):
        try:
            categoryName = item.text.strip()
            categoryURL = item.attrs['href']
            writer.writerow([mainCategoryName, categoryName, categoryURL])

            tmp2 = os.path.exists("lagou2_" + str(i+1) + ".csv")
            c2 = open("lagou2_" + str(i+1) + ".csv", 'a')
            writer2 = csv.writer(c2, lineterminator='\n')
            if tmp2 == False:
                writer2.writerow(["positionName", "company", "salary", "city", "time", "url"])

            res2 = requests.get(categoryURL + "1", headers = headers)
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            maxPage = soup2.select('.pager_container')[0].select('a')[4].text

            #中间层 ---> 工作列表
            for j in range(int(maxPage)):
                res2 = requests.get(categoryURL + str(j+1), headers = headers)
                soup2 = BeautifulSoup(res2.text, 'html.parser')
                for news in soup2.select('.item_con_list li'):
                    url = news.select('.position_link')[0].attrs['href']
                    positionName = news.attrs['data-positionname']
                    company = news.attrs['data-company']
                    salary = news.attrs['data-salary']
                    time = news.select('.format-time')[0].text.strip()
                    city = news.select('em')[0].text.strip()
                    writer2.writerow([positionName, company, salary, city, time, url])
                    

                    tmp3 = os.path.exists("lagou3_" + str(i + 1) + "_" + str(j + 1) + ".csv")
                    c3 = open("lagou3_" + str(i + 1) + "_" + str(j + 1) + ".csv", 'a')
                    writer3 = csv.writer(c3, lineterminator='\n')
                    if tmp3 == False:
                        writer3.writerow(["positionName", "company", "salary", "city", "time", "url"])

                    #最内层 ---> 工作详情
                    res3 = requests.get(url, headers = headers)
                    soup3 = BeautifulSoup(res2.text, 'html.parser')

        except Exception as e:
            raise e
        