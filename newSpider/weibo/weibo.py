from splinter.browser import Browser
from selenium import webdriver
import time

b = Browser(driver_name = 'chrome')
b.visit("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F")
time.sleep(10)
b.find_by_id("loginName").fill("18613723052")
b.find_by_id("loginPassword").fill("5801200")
b.find_by_id("loginAction").click()
time.sleep(10)
b.find_by_value('转发').first.click()
time.sleep(3)
# b.click_link_by_text("发送")

