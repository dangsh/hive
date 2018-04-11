# -*- coding: utf-8 -*-
import scrapy
from huangye88_Company.items import Huangye88CompanyItem

class HycSpider(scrapy.Spider):
    name = 'gg'

    def start_requests(self):
        for i in range(100000):
            url = 'http://www.huangye88.com/product/word%s.html' % str(i+10200000)
            yield scrapy.Request(url=url , callback=self.parse2)
    def parse2(self , response):
        Item = Huangye88CompanyItem()
        if response.status == 200:
            Item["url"] = response.url
        else:
            pass
        # Item["response"] = response.text
        yield Item
    

