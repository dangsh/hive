# -*- coding: utf-8 -*-
from scrapy.conf import settings
from pymongo import MongoClient
from gcpy_utils.spider_utils import  sync_dataflow_push
from gcpy_utils.spider_utils import  async_dataflow_push

class MongopipClass(object):

    # def __init__(self):
    #     client = MongoClient("192.168.14.90" , 27017)
    #     myDb = client["ali"]
    #     self.myCollection = myDb["test_8_15"]
    #     self.myCollection2 = myDb["test_8_15_com"]

    def process_item(self, item, spider):
        # # 如果com_data 不存在，则只处理goods_data
        # if not item["com_data"]:
        #     try:
        #         self.myCollection.insert([item["goods_data"]])
        #     except:
        #         pass
        # else:
        #     try:
        #         self.myCollection.insert([item["goods_data"]])
        #     except:
        #         pass
        #     try:
        #         self.myCollection2.insert([item["com_data"]])
        #     except:
        #         pass

        # if not item["com_data"]:
        #     try:
        #         sync_dataflow_push.dataflow_push("1688_product", item["goods_data"]["source_url"], item["goods_data"])
        #     except:
        #         pass
        # else:
        #     try:
        #         sync_dataflow_push.dataflow_push("1688_product", item["goods_data"]["source_url"], item["goods_data"])
        #     except:
        #         print("update goods error2")
        #         pass
        #     try:
        #         sync_dataflow_push.dataflow_push("1688_company", item["com_data"]["source_url"], item["com_data"])
        #     except:
        #         print("update goods error2")
        #         pass

        if not item["com_data"]:
            try:
                async_dataflow_push.dataflow_push("1688_product", item["goods_data"]["source_url"], item["goods_data"])
            except:
                pass
        else:
            try:
                async_dataflow_push.dataflow_push("1688_product", item["goods_data"]["source_url"], item["goods_data"])
            except:
                print("update goods error2")
                pass
            try:
                async_dataflow_push.dataflow_push("1688_company", item["com_data"]["source_url"], item["com_data"])
            except:
                print("update goods error2")
                pass

        return item




