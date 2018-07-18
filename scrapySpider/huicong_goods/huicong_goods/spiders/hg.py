# -*- coding: utf-8 -*-
import scrapy
import re
from huicong_goods.items import HuicongGoodsItem
import io
import time
from scrapy.exceptions import CloseSpider
import requests
import json

class HgSpider(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = 'hg'
    count = 0
    i = 0
    def start_requests(self):
        with io.open('save.txt', encoding='utf-8') as f:
            stamp = f.read()
        while True:
            stamp2 = str(int(stamp)+self.i)
            self.i += 1
            url = 'https://b2b.hc360.com/supplyself/'+ stamp2 +'.html'
            print(url)
            try:
                yield scrapy.Request(url=url , meta={"stamp":stamp2} , callback=self.parse2)
            except:
                pass
    def parse2(self, response):
        stamp = response.meta["stamp"]
        url = response.url
        if response.status == 404:
            self.count += 1
        if response.status == 200:
            print(self.count)
            if self.count >= 3:
                # 将结果写入文件
                f = open('save.txt', 'w+', encoding='utf-8')
                f.write(stamp)
                f.close()
                #爬虫关闭，将stamp写入文件
                raise CloseSpider('强制停止')
            #有一个200，则将count重置
            self.count = 0
            #获取企业url判断企业是否已被爬取
            com_url = ""
            try:
                com_url = response.xpath('//p[@class="cName"]/a/@href').extract()[0]
            except:
                pass
            if not com_url:
                try:
                    com_url = response.xpath('//div[@class="goods-tit goods-tit-blue"]/a/@href').extract()[0]
                except:
                    pass
            #取出企业的关键词
            com_word = com_url[7:-15]
            test_com_url = 'http://spiderhub.gongchang.com/write_to_online/data_show_onerow?secret=gc7232275&dataset=hc360_company&hkey=http://' + com_word + '.wx.hc360.com/shop/show.html'
            response = requests.get(test_com_url)
            # print(response.text)
            response = json.loads(response.text)
            print(com_url , response["status"])


            # goods_name = response.xpath('//div[@class="proTitCon"]/h1/text()').extract()[0]
            # Item = HuicongGoodsItem()
            # Item["url"] = url
            # Item["goods_name"] = goods_name
            # yield Item
