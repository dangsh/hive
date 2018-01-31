# -*- coding: utf-8 -*-
import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
