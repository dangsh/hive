# -*- coding: utf-8 -*-
import scrapy
import json

class BbSpider(scrapy.Spider):
    name = 'bb'
    start_urls = ['https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid=20141782']

    def parse(self, response):
        response = response.text
        response = json.loads(response)
        page = int(response['data']["page"]["count"])//20 + 1
        for i in range(5):
            url = 'https://api.bilibili.com/x/v2/reply?pn='+ str(i) +'&type=1&oid=20141782'
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self , response):
        response = response.text
        response = json.loads(response)
        mid = len(response['data']['replies'])
        print(mid)