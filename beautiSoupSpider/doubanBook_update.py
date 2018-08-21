# 导入模块
# requests模块用来发起请求
# bs4模块用来解析
# pandas模块用来处理数据，放入excel中
import requests
from bs4 import BeautifulSoup
import pandas
# 声明一个空的list用来存储得到的数据
newsary = []
# 设置UA来防止网站的反爬虫
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# 由于top250一共有250条，每页展示25条，所以一共十页，循环10次
for i in range(10):
    # res是requests请求后返回的页面数据 ， headers = headers 是设置请求头为上面的请求头
    res = requests.get('https://book.douban.com/top250?start=' + str(i*25) , headers = headers)
    # soup 是用来将res.text数据加载成可以解析的格式
    soup = BeautifulSoup(res.text , 'html.parser') 
    #依次取出所需要的数据 ， 详情看word介绍
    for news in soup.select('.item'): #定位
        # 书名
        title = news.select('a')[1].text.replace(' ','')
        # 临时变量a
        a = news.select('p')[0].text
        # 价格
        price = a.split('/')[-1]
        # 出版时间
        time = a.split('/')[-2]
        # 出版社
        store = a.split('/')[-3]
        # 作者名字
        name1 = news.select('p')[0].text.split('/')[:-3][0]
        name2 = ""
        try:
            name2 = "," + news.select('p')[0].text.split('/')[:-3][1]
        except:
            pass;
        # 简介
        jianjie = ""
        try:
            jianjie = news.find_all(class_='inq')[0].text 
        except:
            pass;
        # 评分
        grade = news.select('.rating_nums')[0].text
        # 评价人数
        person = news.find_all(class_='pl')[1].text.replace(' ','').replace('(','').replace(')','')
        # 将得到的数据组成一个字典dict，存入之前定义的newsary中
        newsary.append({'title': title , 'name': name1 + name2 , 'person':person , 'jianjie': jianjie , 'price' : price , 'time' : time , 'store' : store ,'grade':grade})
# 将newsary转换为dataframe类型
newsdf = pandas.DataFrame(newsary)
# 将数据存入excel
newsdf.to_excel('doubanbook.xlsx')