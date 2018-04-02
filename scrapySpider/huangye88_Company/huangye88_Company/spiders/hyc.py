# -*- coding: utf-8 -*-
import scrapy
from huangye88_Company.items import Huangye88CompanyItem

class HycSpider(scrapy.Spider):
    name = 'hyc'

    start_urls = ['http://b2b.huangye88.com/']

    def parse(self , response):
        result = response.text
        for i in response.xpath('//ul[@class="qiyecont"]'):
            urls = i.xpath("li/a/@href").extract()
            for url in urls[:1]:
                yield scrapy.Request(url=url ,  callback=self.parsePlace)


    def parsePlace(self, response):
        for i in response.xpath('//div[@class="main"]/div[1]/div[@class="ad_list"]/a')[:1]:
            firstUrl = i.xpath("@href").extract()
            for url in firstUrl:
                yield scrapy.Request(url=url , callback=self.parseType)

    def parseType(self, response):
        for i in response.xpath('//div[@class="main730"]/div[@class="box"]/ul/li/a'):
            place_type_url = i.xpath("@href").extract_first()
            yield scrapy.Request(url=place_type_url , meta={"url":place_type_url} ,callback=self.get_page)

    def get_page(self , response):
        url = response.meta["url"]
        page = response.css('.box .tit2 span em::text').extract()
        page = int(page[0])//20 + 1
        if page > 1000:
        	page = 1000
        for p in range(page):
            #获取所有页数的url
            newUrl = url + "pn" + str(p+1)
            yield scrapy.Request(url=newUrl , callback=self.get_url)

    def get_url(self , response):
        #找到公司链接
        for i in response.css('#jubao dl dt h4 a'):
            companyUrl = i.xpath('@href').extract_first()  
            Item = Huangye88CompanyItem()
            Item["url"] = companyUrl       
            yield scrapy.Request(url=companyUrl , meta={"item":Item} , callback=self.parse_url)

    def parse_url(self , response):
    	Item = response.meta["item"]
    	response = response.text
    	print(response)


    