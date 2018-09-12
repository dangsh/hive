from selenium import webdriver
import  time
from selenium.webdriver.chrome.options import Options
from gcpy_utils.proxy import adsl
import random

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
for i in range(10000):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')

        result = adsl.get_proxy_list(True)[0]
        temp = '--proxy-server=http://' + result
        chrome_options.add_argument(temp)

        browser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="/python/spiders/music2/chromedriver")
        browser.get("https://music.163.com/#/artist?id=12495660")
        time.sleep(8)
        browser.switch_to.frame(0)
        time.sleep(8)
        btn = browser.find_element_by_xpath('//*[@id="content-operation"]/a[1]')
        btn.click()
        print('success ',i)
        time.sleep(140 + random.randint(1,60))
        browser.close()
    except:
    	pass

