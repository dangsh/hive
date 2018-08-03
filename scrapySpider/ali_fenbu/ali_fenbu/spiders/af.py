# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ali_fenbu.items import AliFenbuItem
class AfSpider(RedisCrawlSpider):
    name = 'af'
    redis_key = 'ali_url'

    def parse(self, response):
        print(response.url)
        pass
