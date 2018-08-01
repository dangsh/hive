# -*- coding: utf-8 -*-
import scrapy
from ali_F.items import AliFItem
class AfSpider(scrapy.Spider):
    name = 'af'

    def start_requests(self):
        with open("goodsid.txt") as f:
            for i in f.readlines():
                code = i.replace('\r','').replace('\n','')
                url = 'https://detail.1688.com/offer/' + code + '.html'
                try:
                    yield scrapy.Request(url=url , callback=self.parse2)
                except:
                    pass

    def parse2(self, response):
        url = response.url
        title = response.xpath('//h1/text()').extract()
        Item = AliFItem()
        Item["url"] = url
        Item["data"] = response.text
        yield Item
