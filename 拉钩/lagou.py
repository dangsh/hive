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
kk = 0
ok = 0
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
     "Cookie":"user_trace_token=20171111142352-da475968-b0c3-4723-9fd2-e09cdda8682d;LGUID=20171111142354-e425554f-c6a8-11e7-88e4-525400f775ce;index_location_city=%E5%85%A8%E5%9B%BD;TG-TRACK-CODE=jobs_code;JSESSIONID=ABAAABAACDBAAIA3AE2D96FBDB51B397D4810F110B8A580;_gat=1; PRE_UTM=;PRE_HOST=;PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FJava%2F%3FlabelWords%3Dlabel; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3812991.html;_gid=GA1.2.1252862149.1510381436;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510381436,1510404510;_ga=GA1.2.412205433.1510381436; LGSID=20171112092509-529da03b-c748-11e7-89d2-525400f775ce;"
}

#最外层 ---> 主页
res = requests.get('https://www.lagou.com/', headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
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
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            maxPage = soup2.select('.pager_container')[0].select('a')[4].text

            #中间层 ---> 工作列表
            for j in range(int(maxPage)):
                res2 = requests.get(categoryURL + str(j+1), headers = headers)
                time.sleep(2)
                soup2 = BeautifulSoup(res2.text, 'html.parser')
                for news in soup2.select('.item_con_list li'):
                    try:
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
                        kk += 1
                        continue

print("-------- OK --------")
print("Error number : ", kk)

        