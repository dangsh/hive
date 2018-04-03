from scrapy.conf import settings
from pymongo import MongoClient


import happybase
class MongopipClass(object):
    
    def __init__(self):
        try:
            self.conn = happybase.Connection('192.168.14.1',9090)
            self.table = self.conn.table("spider_hy88_company")
        except Exception as e:
            pirnt("make connect error %s" % e)
    def process_item(self , item , spider):
        try:
            self.table.put(item["url"] , {"info:content":item["response"]})
        except Exception as e:
            print("insert error %s" %e)
            print("make a new connection")
            self.conn = happybase.Connection('192.168.14.1',9090)
            self.table = self.conn.table("spider_hc360")
        return item
