from splinter.browser import Browser
from selenium import webdriver
import time
import json

def login():
    with open('user.json' , encoding='utf-8') as f:
        for i in range(2):
            line = f.readline()
            d = json.loads(line)
            try:
                print(d['username'] , d['password'])
            except:
                pass
    f.close()

login()
# b = Browser(driver_name = 'chrome')
# b.visit("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F")
# time.sleep(10)
# b.find_by_id("loginName").fill("18613723052")
# b.find_by_id("loginPassword").fill("5801200")
# b.find_by_id("loginAction").click()
# time.sleep(10)
# # b.find_by_value('转发').first.click()
# # time.sleep(3)
# # b.click_link_by_text("发送")
# if b.find_by_text("消息"):
#     b.find_by_text("转发")[0].click()
#     time.sleep(3)
#     b.find_by_css("a")[0].click()
#     print("转发微博成功")
# else:
#     # b.find_by_text("榜单").click()
#     b.find_by_css("h4")[1].click()
#     time.sleep(3)
#     b.find_by_value("发送").click()
#     print("转发微博成功2")
