from splinter.browser import Browser

def login(b):
    print("login")



b = Browser(driver_name = 'chrome')
b.visit("https://weibo.com/")