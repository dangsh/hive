from pymongo import MongoClient

client = MongoClient("localhost" , 27017)
myDb = client["fenbu"]
myCollection = myDb["movies"]

def storeData(name):
    myCollection.insert([{"id":"123" , "moviename":name}])