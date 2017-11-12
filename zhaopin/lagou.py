import requests
from bs4 import BeautifulSoup
import csv 
import os
import time
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
time.sleep(2)
soup = BeautifulSoup(res.text, 'html.parser')
time.sleep(2)
for news in soup.select('.container-body .dn dl'):
    mainCategoryName = news.select('dt')[0].text.strip()
    for i, item in enumerate(news.select('a')):
            categoryName = item.text.strip()
            categoryURL = item.attrs['href']
            writer.writerow([mainCategoryName, categoryName, categoryURL])

            tmp2 = os.path.exists("lagou2_" + str(i+1) + ".csv")
            c2 = open("lagou2_" + str(i+1) + ".csv", 'a')
            writer2 = csv.writer(c2, lineterminator='\n')
            if tmp2 == False:
                writer2.writerow(["positionName", "company", "salary", "city", "time", "url"])

            res2 = requests.get(categoryURL + "1", headers = headers)
            time.sleep(2)
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            maxPage = soup2.select('.pager_container')[0].select('a')[4].text
            time.sleep(2)

            #中间层 ---> 工作列表
            for j in range(int(maxPage)):
                res2 = requests.get(categoryURL + str(j+1), headers = headers)
                time.sleep(2)
                soup2 = BeautifulSoup(res2.text, 'html.parser')
                time.sleep(2)
                for news in soup2.select('.item_con_list li'):
                    url = news.select('.position_link')[0].attrs['href']
                    positionName = news.attrs['data-positionname']
                    company = news.attrs['data-company']
                    salary = news.attrs['data-salary']
                    tim = news.select('.format-time')[0].text.strip()
                    city = news.select('em')[0].text.strip()
                    writer2.writerow([positionName, company, salary, city, tim, url])
                    
                    
                    tmp3 = os.path.exists("lagou3_" + str(i + 1) + ".csv")
                    c3 = open("lagou3_" + str(i + 1) + ".csv", 'a')
                    writer3 = csv.writer(c3, lineterminator='\n')
                    if tmp3 == False:
                        writer3.writerow(["jobName", "city", "company", "salary", "workMode", "degree", "experience", "jobCategory","companyName", "companyField", "companyDevelopmentStage", "companySize", "companyURL", "jobAdvantage", "jobDescription"])
                    #最内层 ---> 工作详情
                    res3 = requests.get(url, headers = headers)
                    time.sleep(2)
                    soup3 = BeautifulSoup(res3.text, 'html.parser')
                    time.sleep(2)
                    try:
                        company = soup3.select('.position-content-l .company')[0].text.strip()
                        jobName = soup3.select('.job-name .name')[0].text.strip()
                        salary = soup3.select('.job_request span')[0].text.replace("/", '').strip()
                        city = soup3.select('.job_request span')[1].text.replace("/", '').strip()
                        experience = soup3.select('.job_request span')[2].text.replace("/", '').strip()
                        degree = soup3.select('.job_request span')[3].text.replace("/", '').strip()
                        workMode = soup3.select('.job_request span')[4].text.replace("/", '').strip()
                        jobCategory = ""
                        for val in soup3.select('.position-label li'):
                            jobCategory += val.text.strip() + ";"
                        jobAdvantage = soup3.select('.job-advantage p')[0].text.strip()
                        jobDescription = ""
                        # print(soup3.select('.job_bt p'))
                        for val in soup3.select('.job_bt p'):
                            # print(val.text.strip())
                            if val.text.strip() != "":
                                jobDescription += val.text.strip() + "&&"
                        companyName = soup3.select('.b2')[0].attrs['alt']
                        companyField = soup3.select('.c_feature li')[0].text.split('\n')[1].strip()
                        companyDevelopmentStage = soup3.select('.c_feature li')[1].text.split('\n')[1].strip()
                        companySize = soup3.select('.c_feature li')[2].text.split('\n')[1].strip()
                        companyURL = soup3.select('.c_feature a')[0].text.strip()
                        workAddrList = soup3.select('.work_addr')[0].text.split('\n')
                        workAddr = ""
                        for wAddr in workAddrList:
                            workAddr += wAddr.strip()
                        workAddr = workAddr[0:-4]
                        data = [jobName, city, company, salary, workMode, degree, experience, jobCategory,companyName, companyField, companyDevelopmentStage, companySize, companyURL, jobAdvantage, jobDescription]
                        # print(data)
                        writer3.writerow(data)
                    except:
                        continue

        