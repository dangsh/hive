#-*- coding:utf-8 -*-
#京东抢手机脚本
from splinter.browser import Browser
import time

#登录页
def login(b):  #登录京东
    b.click_link_by_text("你好，请登录")
    time.sleep(3)
    b.click_link_by_text("账户登录")
    b.fill("loginname","18613723052")  #填写账户密码
    b.fill("nloginpwd","961124zxg")
    b.find_by_id("loginsubmit").click()
    time.sleep(3)
    return b
    

b=Browser(driver_name="chrome") #打开浏览器
b.visit("https://item.jd.com/5853593.html")
login(b)

while True:
    try:
        b.click_link_by_text("立即抢购")
        try:
            if b.title=="商品已成功加入购物车":
                print("加入购物车成功")
                break
            else:  #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页
                b.visit("https://item.jd.com/5853593.html")
                b.click_link_by_text("立即抢购")
                time.sleep(1)
                break
        except Exception as e: #异常情况处理，以免中断程序
            b.reload() 
            time.sleep(2)
            break
            
    except:
        print("没找到抢购按钮")
