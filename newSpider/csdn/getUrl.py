import requests
from lxml import etree


def getThis():
    response = requests.get('http://blog.csdn.net/dangsh_')
    selector = etree.HTML(response.text)
    url = selector.xpath('//ul[@class="detail"]/li[2]/ul[2]/li/a/@href')
    return url