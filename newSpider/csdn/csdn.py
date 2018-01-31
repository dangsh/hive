from splinter.browser import Browser
from selenium import webdriver
import time
from conn import getIp

# b=Browser(driver_name="chrome") #打开浏览器
# b.visit("http://blog.csdn.net/dangsh_/article/details/79221328")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/79214246")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/79195230")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/79166691")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/79122584")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/78646856")
# time.sleep(4)

# b.visit("http://blog.csdn.net/dangsh_/article/details/78504068")
# time.sleep(4)

ip = getIp()
try:
    for i in ip:
        ip = str(i[0]) + ':' + str(i[1])
        chrome_options = webdriver.ChromeOptions()
        temp = '--proxy-server=http://' + ip
        chrome_options.add_argument(temp)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://blog.csdn.net/dangsh_/article/details/79221328") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/79214246") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/79195230") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/79166691") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/79122584") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/78646856") 
        time.sleep(3)

        driver.get("http://blog.csdn.net/dangsh_/article/details/78504068") 
        time.sleep(3)

        driver.close()

except:
    pass
