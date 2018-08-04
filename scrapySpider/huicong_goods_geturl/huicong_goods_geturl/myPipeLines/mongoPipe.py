# -*- coding: utf-8 -*-
from scrapy.conf import settings
import redis

class MongopipClass(object):
    def __init__(self):
        self.r = redis.Redis(host='192.168.8.186', port='6379', db=0, decode_responses=True)
    def process_item(self , item , spider):
        #将url存入redis
        self.r.lpush("goods_url", item["url"])
        return item




