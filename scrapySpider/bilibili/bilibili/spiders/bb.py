# -*- coding: utf-8 -*-
import scrapy
import json
from bilibili.items import BilibiliItem
class BbSpider(scrapy.Spider):
    name = 'bb'
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Host':'space.bilibili.com',
        'Origin':'https://space.bilibili.com',
        'Referer':'https://space.bilibili.com/5723630/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }       

    """不抓html页面了，请求接口
                https://space.bilibili.com/ajax/member/GetInfo
                post请求，提交的数据为
                mid:1
                csrf:82bdff2b4cf8a131c67355f4c5daf334"""
    def start_requests(self):
        for i in range(1000000):
            url = 'https://space.bilibili.com/ajax/member/GetInfo'
            userid = str(i+1)
            yield scrapy.FormRequest(
                url = url,
                headers=self.headers ,
                formdata = {"mid" : userid, "csrf" : "abf720efaefa71105e20141979f3ca81"},
                callback = self.parse2
            )

    def parse2(self , response):
        response = response.text
        response = json.loads(response)
        mid = response["data"]["mid"]
        username = response["data"]["name"]
        head_img = response["data"]["face"]
        register_time = response["data"]["regtime"]
        birthday = response["data"]["birthday"]
        place = response["data"]["place"]
        # print(mid,username,head_img,register_time,birthday,place)
        Item = BilibiliItem()
        Item["userid"] = mid 
        Item["username"] = username
        Item["head_img"] = head_img
        Item["register_time"] = register_time
        Item["birthday"] = birthday
        Item["place"] = place
        yield Item

