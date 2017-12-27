from scrapy.conf import settings
from pymongo import MongoClient



class MongopipClass(object):
    
    def __init__(self):
        client = MongoClient(settings["MONGO_HOST"] , settings["MONGO_PORT"])
        myDb = client[settings["MONGO_DBNAME"]]
        self.myCollection = myDb[settings["MONGO_COLLECTION"]]

    def process_item(self , item , spider):
        self.myCollection.insert([{'companyName':item["companyName"] , 'companyLocal':item['companyLocal'] , 'companyType':item["companyType"] , 'companyProduct':item["companyProduct"] ,'lianxiren':item["lianxiren"] ,'telephone':item["telephone"] ,  'zhuye':item["zhuye"] }])

        return item
    