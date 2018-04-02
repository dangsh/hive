# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from fenbu.items import FenbuItem
import re
import redis


class MoviespiderSpider(RedisCrawlSpider):
    name = 'ff'
    redis_key = 'fenbuSpider:start_urls'

    def parse(self , response):
        print(response.text)