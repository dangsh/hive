import requests
from bs4 import BeautifulSoup
import pandas
import time

try:
    newsary = []
    gongzuo = []
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' , 'Cookie':'user_trace_token=20170823200708-9624d434-87fb-11e7-8e7c-5254005c3644; LGUID=20170823200708-9624dbfd-87fb-11e7-8e7c-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=5c26ebb801b5138a9e3541efa53d578f; JSESSIONID=ABAAABAAAGGABCB26465ACEC8C33DC643C41A997C9C3D3D; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dyt4OP0uCR8_QwkrJLeR61l5NzSiPJ4uxlYWR_uq_TIK%26wd%3D%26eqid%3Dc1c7e7270003b5de000000035a079fed; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=0bc578f8a548496dbec964f7759a2a29; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510383830,1510449045,1510449059,1510449145; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510449145; _ga=GA1.2.845768630.1503490030; _gid=GA1.2.1076093348.1510383830; LGSID=20171112091220-87f8d126-c746-11e7-98b7-5254005c3644; LGRID=20171112091224-8a94136d-c746-11e7-98b7-5254005c3644'}
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


    gongzuo = gongzuo[:20]

    for j in gongzuo:
        print(j)
        for i in range(10):
            time.sleep(4)
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
except:
    newsdf = pandas.DataFrame(newsary)
    newsdf.to_excel('lagouPlusp3.xlsx')


newsdf = pandas.DataFrame(newsary)
newsdf.to_excel('lagouPlusp3.xlsx')



# print(gongzuo)