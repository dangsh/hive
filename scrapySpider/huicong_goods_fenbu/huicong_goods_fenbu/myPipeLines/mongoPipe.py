# -*- coding: utf-8 -*-
from scrapy.conf import settings
from pymongo import MongoClient
from gcpy_utils.spider_utils import  sync_dataflow_push


class MongopipClass(object):

    def __init__(self):
        client = MongoClient(settings["MONGO_HOST"] , settings["MONGO_PORT"])
        myDb = client[settings["MONGO_DBNAME"]]
        self.myCollection = myDb[settings["MONGO_COLLECTION"]]
        self.myCollection2 = myDb["huicong_com2"]

    def process_item(self, item, spider):
        #如果com_data 不存在，则只处理goods_data
        if not item["com_data"]:
            try:
                self.myCollection.insert([item["goods_data"]])
            except:
                pass
        else:
            try:
                self.myCollection.insert([item["goods_data"]])
            except:
                pass
            try:
                self.myCollection2.insert([item["com_data"]])
            except:
                pass

        return item




