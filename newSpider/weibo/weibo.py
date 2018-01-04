from splinter.browser import Browser
from selenium import webdriver
import time
import json
import requests

#从user.json中读取账号信息，num为读取第几条账号
def login(num):
    with open('user.json' , encoding='utf-8') as f:
        lines = f.readlines()
        line = lines[num:]
        d = json.loads(line[0])
        try:
            # print(d['username'] , d['password'])
            return d['username'] , d['password']
        except:
            pass
    f.close()

#微博转发方法
def forward(b):
    if b.find_by_text("消息"):
        time.sleep(5)
        try:
            b.find_by_text("转发")[0].click()
            time.sleep(3)
            b.find_by_css("a")[0].click()
            print("转发微博成功")
        except:
            print("转发微博出错")
    else:
        try:
            b.find_by_css("h4")[1].click()
            time.sleep(3)
            b.find_by_css("a")[0].click()
            print("转发微博成功2")
        except:
            print("转发微博出错2")

#没有“转发”两个字，有转发数量
def oneForward(b):
    try:
        # b.find_by_text("榜单").click()
        b.find_by_css("h4")[1].click()
        time.sleep(3)
        b.find_by_css("a")[0].click()
        print("转发微博成功2")
    except:
        print("转发微博出错2")

#有“转发”两个字
def oneForward2(b):
    try:
        b.find_by_text("转发")[0].click()
        time.sleep(3)
        b.find_by_css("a")[0].click()
        print("转发微博成功")
    except:
        print("转发微博出错")

#通过ip代理获取ip
def getIp():
    all_url = [] # 存储IP地址的容器
    # 代理IP的网址
    url = "http://api.xicidaili.com/free2016.txt"
    r = requests.get(url=url)
    print(r.text)
    # all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+",r.text)
    # with open("D:\\code\\python\\new\\Brush ticket\\IP.txt",'w') as f:
    #     for i in all_url:
    #         f.write(i)
    #         f.write('\n')
    # return all_url

#转发特定微博
def forwardMoney(b):
    time.sleep(10)
    b.visit("https://m.weibo.cn/1255795640/4192089996527286")
    time.sleep(10)
    oneForward(b)

for i in range(3):
    username , password = login(i)
    b = Browser(driver_name = 'chrome')
    b.visit("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F")
    time.sleep(10)
    b.find_by_id("loginName").fill(username)
    b.find_by_id("loginPassword").fill(password)
    b.find_by_id("loginAction").click()
    time.sleep(10)
    forward(b)
    time.sleep(10)
    b.quit()
    time.sleep(10)


