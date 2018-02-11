# -*- coding: utf-8 -*-
import scrapy
import json
from weibo.items import WeiboItem
import time

class WiwiSpider(scrapy.Spider):
    count = 1
    name = 'ozzy'
    start_urls = ['http://www.baidu.com']

    cookie = {
        'T_WM' : '6f33fb05e2825da195d0d8a6bb2c1c21',
        'SCF' : 'AvOqQOQouYuqAqpXBdvflU6utIfkJOWAVWbxzfMTv9j0Rg4G - wmUILsLjnzZCdb6pH5frhsKWxrut4hANcM - 2FM.',
        'SUB' : '_2A253etQMDeRhGeBM61EY8irEyzSIHXVUhPxErDV6PUJbkdAKLRjwkW1NRQw8HJf_5QkMzzCj - zPl - Xu6TGlqc5kJ',
        'WEIBOCN_WM' : '90112_90001',
        'WEIBOCN_FROM' : '1110006030',
        'M_WEIBOCN_PARAMS' : 'featurecode % 3DH5tuiguang0623 % 26oid % 3D4205574042439353 % 26luicode % 3D10000011 % 26lfid % 3D102803 % 26uicode % 3D20000061 % 26fid % 3D4205574042439353'
    }

    # start_urls 没有用，第一次parse只负责拼接url，获取weibo信息列表
    def parse(self, response):
        for i in range(1000):
            url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803&client=h5&featurecode=H5tuiguang0623&need_head_cards=1&wm=90112_90001&since_id='+ str(i+1)
            try:
                yield scrapy.Request(url=url ,cookies=self.cookie ,callback=self.parse2)
            except:
                pass

    # 第二次解析数据，获取到微博内容的id
    def parse2(self , response):
        response = response.text
        response = json.loads(response)
        for i in range(len(response['data']['cards'])):
            weiboId = response['data']['cards'][i]['mblog']['id']
            # Item = WeiboItem()
            # Item["weiboid"] = weiboId
            url = 'https://m.weibo.cn/api/comments/show?id=' + weiboId + '&page=2'
            # yield Item
            yield scrapy.Request(url=url ,cookies=self.cookie , meta={"weiboid":weiboId} , callback=self.parse3)

    #第三次解析获取评论的页数
    def parse3(self , response):
        weiboid = response.meta["weiboid"]
        response = response.text
        response = json.loads(response)
        page = 2
        try:
            page = response['data']['max']
        except:
            pass
        # Item = WeiboItem()
        # Item["page"] = page
        # Item["weiboid"] = weiboid
        if page > 100:
            page = 100
        for i in range(page-1):
        # for i in range(10):
            url = 'https://m.weibo.cn/api/comments/show?id=' + weiboid + '&page='+ str(2+i)
            yield scrapy.Request(url=url, cookies=self.cookie, callback=self.parse4)
        # yield Item

    #第四次解析获取评论者的id
    def parse4(self , response):
        response = response.text
        response = json.loads(response)
        # print(response)  #这里有可能是暂无数据

        # print(len(response['data']['data']))
        for i in range(len(response['data']['data'])):
            userid = response['data']['data'][i]['user']['id']
            username = response['data']['data'][i]['user']['screen_name']
            Item = WeiboItem()
            Item["userid"] = userid
            Item["username"] = username
        yield Item

    #第五次解析获取评论者的信息
    def parse5(self , response):
        pass

