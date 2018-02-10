from splinter.browser import Browser
from selenium import webdriver
import time
from conn import getIp
from getUrl import getThis
import random

ip = getIp()
someIp = random.sample(ip , 10)
try:
    for i in ip:
        ip = str(i[0]) + ':' + str(i[1])
        chrome_options = webdriver.ChromeOptions()
        temp = '--proxy-server=http://' + ip
        chrome_options.add_argument(temp)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        url = getThis()
        someUrl = random.sample(url , 3)
        for i in someUrl:
            driver.get(i) 
            time.sleep(3)
        driver.close()

except:
    pass
