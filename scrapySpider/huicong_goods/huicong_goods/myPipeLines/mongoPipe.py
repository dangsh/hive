# -*- coding: utf-8 -*-
from scrapy.conf import settings
from pymongo import MongoClient



class MongopipClass(object):
    
    def __init__(self):
        client = MongoClient(settings["MONGO_HOST"] , settings["MONGO_PORT"])
        myDb = client[settings["MONGO_DBNAME"]]
        self.myCollection = myDb[settings["MONGO_COLLECTION"]]
        self.myCollection2 = "huicong_com"

    def process_item(self , item , spider):
        # try:
        #     self.myCollection.insert([{'_id':item["url"] , 'goods_name':item["goods_name"]}])
        # except:
        #     pass
        #如果com_data 不存在，则只处理goods_data
        if not item["com_data"]:
            try:
                self.myCollection.insert([item["goods_data"]])
            except:
                pass
        else:
            #处理goods_data 和 com_data
            try:
                self.myCollection.insert([item["goods_data"]])
            except:
                pass
            try:
                self.myCollection2.insert([item["com_data"]])
            except:
                pass
            pass
        return item
#

# import happybase
# class MongopipClass(object):
#
#     def __init__(self):
#         self.conn = happybase.Connection('192.168.14.1',9090)
#
#     def process_item(self , item , spider):
#         try:
#             self.table = conn.table("spider_hc360")
#             self.table.put(item["url"] , {"info:content":item["response"] , "info:data":item["data"]})
#         except:
#             pass
#         return item




