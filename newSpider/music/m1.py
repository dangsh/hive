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


# browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
browser.get("https://music.163.com/#/artist?id=12495660")
time.sleep(20)
browser.switch_to.frame(0)
time.sleep(20)
browser.save_screenshot('1.png')
btn = browser.find_element_by_xpath('//*[@id="content-operation"]/a[1]')
btn.click()
print('success ')
time.sleep(10)
browser.close()

