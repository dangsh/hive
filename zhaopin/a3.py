import requests
from bs4 import BeautifulSoup
import csv 
import os
tmp3 = os.path.exists("lagou3_1.csv")
c3 = open("lagou3_1.csv", 'a')
writer3 = csv.writer(c3, lineterminator='\n')
if tmp3 == False:
    writer3.writerow(["jobName", "city", "company", "salary", "workMode", "degree", "experience", "jobCategory","companyName", "companyField", "companyDevelopmentStage", "companySize", "companyURL", "jobAdvantage", "jobDescription"])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

#最外层 ---> 主页
res3 = requests.get('https://www.lagou.com/jobs/1939134.html', headers = headers)
soup3 = BeautifulSoup(res3.text, 'html.parser')
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
except Exception as e:
    raise e

# mainCategoryName = news.select('dt')[0].text.strip()
# for i, item in enumerate(news.select('a')):
#     try:
#         categoryName = item.text.strip()
#         categoryURL = item.attrs['href']
#         writer3.writerow([mainCategoryName, categoryName, categoryURL])
#     except Exception as e:
#             raise e