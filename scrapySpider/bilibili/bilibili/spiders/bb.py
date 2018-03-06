# -*- coding: utf-8 -*-
import scrapy
import json

class BbSpider(scrapy.Spider):
    name = 'bb'
    start_urls = ['http://www.ip181.com/']

    # def parse(self, response):
    #     response = response.text
    #     response = json.loads(response)
    #     page = int(response['data']["page"]["count"])//20 + 1
    #     for i in range(5):
    #         url = 'https://api.bilibili.com/x/v2/reply?pn='+ str(i) +'&type=1&oid=20141782'
    #         yield scrapy.Request(url=url, callback=self.parse2)

    # def parse2(self , response):
    #     response = response.text
    #     response = json.loads(response)
    #     mid = len(response['data']['replies'])
    #     print(mid)

    # def parse(self , response):
    #     #总共2 5700 0000 位用户
    #     for i in range(10):
    #         url = 'https://space.bilibili.com/' + str(i+1)
    #         print(url)
    #         yield scrapy.Request(url=url ,  callback=self.parse2)

    # def parse2(self , response):
    #     response = response.text
    #     print(response)


    不抓html页面了，请求接口
    https://space.bilibili.com/ajax/member/GetInfo
    post请求，提交的数据为
    mid:1
    csrf:82bdff2b4cf8a131c67355f4c5daf334
