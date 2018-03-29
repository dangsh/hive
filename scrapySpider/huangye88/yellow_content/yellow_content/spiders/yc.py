# -*- coding: utf-8 -*-
import scrapy
import json
from yellow_content.items import YellowContentItem

class YcSpider(scrapy.Spider):
    name = 'yc'
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        with open('data.json', encoding='utf-8') as f:
            for i in range(2000):
                url = f.readline().strip('\n')
                new_url = json.loads(url)
                a = new_url["url"]
                try:
                    yield scrapy.Request(url=a , meta = {"url" : a} , callback=self.parse2)
                except:
                    pass

    def parse2(self , response):
        url = response.meta["url"]
        response = response.text
        Item = YellowContentItem()
        Item["_id"] = url
        Item["content"] = response
        yield Item
