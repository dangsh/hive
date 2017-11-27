# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
from mongoTest.items import MongotestItem
from scrapy import Request


class TestSpider(scrapy.Spider):
    name = 'test'
    
    start_urls = ['https://www.douban.com/doulist/36980/']
    # db = MongoClient("127.0.0.1" , 27017)

    # myDb = db["mongo"]
    # students = myDb["worker"]

    def parse(self, response):


        for item in response.css(".doulist-subject .title"):
            print("(((((((((((((((((((((((")
            movieName = item.xpath("a/text()").extract()
            

            it = MongotestItem()
            it["movieName"] = movieName
            yield it


            
            # TestSpider.students.insert({'name':movieName , 'age':13})



        
