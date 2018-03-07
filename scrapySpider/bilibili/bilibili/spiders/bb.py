# -*- coding: utf-8 -*-
import scrapy
import json

class BbSpider(scrapy.Spider):
    name = 'bb'
    start_urls = ['http://www.ip181.com/']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://space.bilibili.com/45388',
        'Origin': 'http://space.bilibili.com',
        'Host': 'space.bilibili.com',
        'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }


    """不抓html页面了，请求接口
                https://space.bilibili.com/ajax/member/GetInfo
                post请求，提交的数据为
                mid:1
                csrf:82bdff2b4cf8a131c67355f4c5daf334"""

    def parse(self , response):
        for i in range(10):
            url = 'https://space.bilibili.com/ajax/member/GetInfo'
            userid = str(i+1)
            yield scrapy.FormRequest(
                url = url,
                # cookies=self.cookie ,
                headers=self.headers ,
                formdata = {"mid" : userid, "csrf" : "abf720efaefa71105e20141979f3ca81"},
                callback = self.parse2
            )

    def parse2(self , response):
        response = response.text
        response = json.loads(response)
        print(response["data"]["mid"] , response["data"]["name"])
