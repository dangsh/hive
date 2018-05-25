# -*- coding: utf-8 -*-
import scrapy
import re
from huicong_com.items import HuicongComItem
import io

class HccSpider(scrapy.Spider):
    name = 'hcc'
    def start_requests(self):
        url = ''
        word = ''
        with io.open('level3.txt', encoding='utf-8') as f:
            for i in f.readlines():
                word = i.replace('\n','')
                url = 'https://s.hc360.com/?w='+ word +'&mc=enterprise'
                try:
                    yield scrapy.Request(url=url , callback=self.parse2)
                except:
                    pass
    def parse2(self, response):
        reg = '<span class="total">共(.*?)页</span>'
        page = re.findall(reg, response.text)
        if page:
            page = page[0]
        if not page:
            page = 10
        for i in range(int(page)):
            new_url = response.url + "&ee=" + str(i + 1)
            try:
                yield scrapy.Request(url=new_url , meta={"new_url":new_url}, callback=self.parse3)
            except:
                pass
    def parse3(self, response):
        new_url = response.meta["new_url"]
        new_url = new_url + "&af=1"
        data = response.xpath('//dd[@class="til"]/h3/a/@href').extract()
        try:
            yield scrapy.Request(url=new_url , meta={"data":data} , callback=self.parse4)
        except:
            pass
    def parse4(self, response):
        data = response.meta["data"]
        data2 = response.xpath('//dd[@class="newName"]/a/@href').extract()
        data3 = []
        for i in data2:
            i = 'http:'+i
            data3.append(i)
        data = data + data3
        for i in data:
            Item = HuicongComItem()
            Item["url"] = i
            yield Item


