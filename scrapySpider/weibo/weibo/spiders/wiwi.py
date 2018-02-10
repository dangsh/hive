# -*- coding: utf-8 -*-
import scrapy
import json
from weibo.items import WeiboItem
import time

class WiwiSpider(scrapy.Spider):
    count = 1
    name = 'wiwi'
    start_urls = ['https://m.weibo.cn/api/comments/show?id=4205450222107594&page=1']

    def parse(self, response):
        for i in range(100):
            url = 'https://m.weibo.cn/api/comments/show?id=4205450222107594&page='+ str(i+1)
            # try:
            yield scrapy.Request(url=url,callback=self.parse2)
            # except:
            #     pass

    def parse2(self , response):
        response = response.text
        response = json.loads(response)
        for i in range(len(response['data']['data'])):
            userid = response['data']['data'][i]['user']['id']
            username = response['data']['data'][i]['user']['screen_name']
            # print(userid, username)
            Item = WeiboItem()
            Item["userid"] = userid
            Item["username"] = username
            self.count = self.count + 1
            print(self.count)
            time.sleep(1)
            yield Item
