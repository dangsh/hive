# -*- coding: utf-8 -*-
import scrapy


class BbSpider(scrapy.Spider):
    name = 'bb'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
