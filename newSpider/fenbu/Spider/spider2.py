import requests
import re
from utils.linkMongo import storeData

def getCntent(url):
    # print(url)
    print("线程2")
    reg = '<span property="v:itemreviewed">(.*?)</span>'
    response = requests.get(url)
    response = response.text
    result = re.findall(reg , response)
    storeData(result)