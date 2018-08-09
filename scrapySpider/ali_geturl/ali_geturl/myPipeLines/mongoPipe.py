# -*- coding: utf-8 -*-
from scrapy.conf import settings
import redis
from pymongo import MongoClient

# class MongopipClass(object):
#     def __init__(self):
#         self.r = redis.Redis(host='192.168.8.186', port='6379', db=1, decode_responses=True)
#
#     def process_item(self, item, spider):
#         # 将url存入redis
#         self.r.lpush("ali_url", item["url"])
#         return item


class MongopipClass(object):

    def __init__(self):
        client = MongoClient("192.168.14.90" , 27017)
        myDb = client["ali"]
        self.myCollection = myDb["goodsid_8_9"]

    def process_item(self, item, spider):
        try:
            self.myCollection.insert([{"_id":item["url"]}])
        except:
            pass

        return item
