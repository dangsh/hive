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

def loop(b):
    try:
        b.click_link_by_text("立即抢购")
        if b.title=="商品已成功加入购物车":
            print("加入购物车成功")
        else:  #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页
            print("抢购出错")
            # b.visit("https://item.jd.com/6086957.html")
            b.visit("https://item.jd.com/4993751.html")
            time.sleep(3)
            b.click_link_by_text("立即抢购")
    except:
        print("没找到抢购按钮")
        b.reload()
        time.sleep(2)
        loop(b)

b=Browser(driver_name="chrome") #打开浏览器
b.visit("https://item.jd.com/4993751.html")
time.sleep(2)
login(b)
time.sleep(10)
loop(b)


