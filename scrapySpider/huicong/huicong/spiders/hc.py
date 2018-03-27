# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from huicong.items import HuicongItem
import re
import redis


class MoviespiderSpider(RedisCrawlSpider):
    name = 'hcc'
    redis_key = 'hcSpider:start_urls'

    def parse(self , response):
        url = response.url
        # https://b2b.hc360.com/supplyself/611981061.html
        data1 = response.text
        reg = '/(\d+)'
        goodsid = re.findall(reg , url)
        goodsid = goodsid[0]
        # Item = HuicongItem()
        # Item["url"] = url
        # Item["response"] = data1
        # yield Item
        new_url = 'https://wsdetail.b2b.hc360.com/XssFilter?bcid=%s'% goodsid
        yield scrapy.Request(url=new_url , meta={"url":url , 'data1':data1} ,callback=self.parse2)

    def parse2(self , response):
    	url = response.meta["url"]
    	data1 = response.meta["data1"]
    	data2 = response.text
    	Item = HuicongItem()
    	Item["url"] = url
    	Item["response"] = data1
    	Item["data"] = data2
    	yield Item