# from splinter.browser import Browser
# import time
#
# b = Browser(driver_name = 'chrome')
# b.visit("https://music.163.com/#/song?id=1307440707")
# time.sleep(5)
# b.find_by_xpath('//*[@id="content-operation"]/a[1]').first().click()
# time.sleep(3)
# b.quit()

from selenium import webdriver
import  time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
for i in range(10000):
    try:
        browser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="/python/spiders/music2/chromedriver")
        browser.get("https://music.163.com/#/artist?id=12495660")
        time.sleep(8)
        browser.switch_to.frame(0)
        time.sleep(8)
        btn = browser.find_element_by_xpath('//*[@id="content-operation"]/a[1]')
        btn.click()
        print('success ',i)
        time.sleep(10)
        browser.close()
    except:
    	pass

