from splinter.browser import Browser
import time

def login(b):
    print("login")



b = Browser(driver_name = 'chrome')
b.visit("https://weibo.com/")
time.sleep(10)
b.fill('username' , '123')
b.fill('password' , '123')
b.click_link_by_text("登录")

