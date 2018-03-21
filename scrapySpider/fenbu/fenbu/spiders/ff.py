# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import re

class FfSpider(RedisSpider):
    name = 'ff'
    redis_key = 'Search:start_urls'


    def parse(self , response):
        response = response.text
        reg = '.html\?offerId=([0-9]*)'
        data = re.findall(reg , response)
        print(data)