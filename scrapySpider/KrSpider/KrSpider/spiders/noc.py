# -*- coding: utf-8 -*-
import scrapy
from KrSpider.items import KrspiderItem

class NocSpider(scrapy.Spider):
    name = 'noc'
    start_urls = ['http://36kr.com/']

    def parse(self, response):
        # print(response.body.decode())
        for item in response.xpath('//ul[@class="feed_ul"]/li/div/a/div[@class="intro"]'):
            title = item.xpath('h3/text()').extract()
            content = item.xpath('div/text()').extract()
            
            oneItem = KrspiderItem()
            oneItem["title"] = title
            oneItem["content"] = content

            yield oneItem
        pass
