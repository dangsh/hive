import requests
from gcpy_utils.proxy import adsl
while True:
    result = adsl.get_proxy_list(True)[0]
    my_proxy = "http://" + result
    proxies = {"http":my_proxy}
    response = requests.get("http://www.4399.com", proxies=proxies, verify=False)
    print my_proxy,response