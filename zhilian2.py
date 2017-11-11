import requests
from bs4 import BeautifulSoup
import csv
import os

tmp = os.path.exists("zhilian.csv")
c = open("zhilian.csv","a")
writer = csv.writer(c, lineterminator='\n')
if tmp == False:
    writer.writerow(["companyName", "companyIndustry", "recruitmentType", "jobName", "jobCity", "jobPeopNum", "releaseTime", "companySize", "companyType", "positionCategory",  "jobURL"])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
for i in range(200):
    res = requests.get('https://xiaoyuan.zhaopin.com/full/538/0_0_0_0_0_-1_0_' + str(i) + '_0' , headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    for news in soup.select('.searchResultListUl li'):
        #公司名
        try:
            companyName = news.select('span')[0].text.strip()
            #公司行业(/分隔)
            companyIndustry = news.select('p')[1].text.strip()
            #招聘类型(校园招聘/社会招聘)
            recruitmentType = news.select('span')[1].text.strip()
            #职位
            jobName = news.select('a')[0].text.strip()
            #工作城市
            jobCity = news.select('em')[0].text.strip()
            #招收人数
            jobPeopNum = news.select('em')[1].text.strip()
            #发布时间
            # releaseTime = news.select('.searchResultKeyval span')[2].text.strip().split("：")[1]
            #详情链接
            jobURL = news.select('a')[0].attrs['href']
            res2 = requests.get('https:' + jobURL , headers = headers)
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            #公司规模
            companySize = soup2.select('.cJobDetailInforTopWrap li')[5].text.strip()
            #公司类型
            companyType = soup2.select('.cJobDetailInforTopWrap li')[7].text.strip()
            #职位类别
            positionCategory = soup2.select('.cJobDetailInforBotWrap li')[3].text.strip()
            #发布时间
            releaseTime = soup2.select('.cJobDetailInforBotWrap li')[7].text.strip()


            data = [companyName, companyIndustry, recruitmentType, jobName, jobCity, jobPeopNum, releaseTime, companySize, companyType, positionCategory, jobURL]
            writer.writerow(data)
        except:
            pass









