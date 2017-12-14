# -*- coding: utf-8 -*-
import scrapy


class NocSpider(scrapy.Spider):
    name = 'noc'
    start_urls = ['http://36kr.com/']

    def parse(self, response):
        print(response)
