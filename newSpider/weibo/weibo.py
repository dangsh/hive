from splinter.browser import Browser
from selenium import webdriver
import time

# b = Browser(driver_name = 'chrome')
# b.visit("https://weibo.com/")
# time.sleep(10)
# b.fill('username' , '123')
# b.fill('password' , '123')
# b.click_link_by_text("你好，请登录")

browser = webdriver.Chrome()
#设置浏览器加载超时时间
browser.set_page_load_timeout(30)
loginUrl = "https://weibo.com/"
browser.get(loginUrl)

try:
    browser.find_element_by_xpath('//*[@name="username"]').send_keys('13096925043')
    print('user success!')
except:
    print('user error!')
time.sleep(1)

try:
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('c2ptymvr')
    print('pw success!')
except:
    print('pw error!')
time.sleep(1)

try:
    browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    print('click success!')
except:
    print('click error!')
time.sleep(30)