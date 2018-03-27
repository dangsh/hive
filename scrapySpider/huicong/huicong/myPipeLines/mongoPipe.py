# from scrapy.conf import settings
# from pymongo import MongoClient



# class MongopipClass(object):
    
#     def __init__(self):
#         client = MongoClient(settings["MONGO_HOST"] , settings["MONGO_PORT"])
#         myDb = client[settings["MONGO_DBNAME"]]
#         self.myCollection = myDb[settings["MONGO_COLLECTION"]]

#     def process_item(self , item , spider):
#         try:
#             self.myCollection.insert([{'_id':item["url"] , 'response':item["response"] , 'data':item["data"]}])
#         except:
#             pass
#         return item
#     
import happybase

class MongopipClass(object):
    
    def __init__(self):
        self.conn = happybase.Connection('192.168.14.1',9090)

    def process_item(self , item , spider):
        try:
            self.table = conn.table("spider_hc360")
            self.table.put(item["url"] , {"info:content":item["response"] , "info:data":item["data"]})
        except:
            pass
        return item



# import happybase
# conn = happybase.Connection('192.168.14.1',9090)
# table = conn.table("spider_hc360")
# def write_data_to_db(url , response , data):
#     table.put(url , {"info:content":response , "info:data":data})

# if __name__ == "__main__":
#     write_data_to_db(item["url"] , item["response"] , item["data"])

