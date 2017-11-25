# -*- coding: utf-8 -*-
import scrapy


class MidSpider(scrapy.Spider):
    name = 'mid'

    start_urls = ['http:////wap.jd.com/category/all.html/']

    def parse(self , response):
        for item in response.css(".mc"):
            title = item.css(".p-name a::text").extract()
            print(title)
        

