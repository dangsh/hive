# -*- coding: utf-8 -*-
import scrapy
import re
from huicong_goods.items import HuicongGoodsItem
import io
import time
from scrapy.exceptions import CloseSpider

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
            goods_name = response.xpath('//div[@class="proTitCon"]/h1/text()').extract()[0]
            Item = HuicongGoodsItem()
            Item["url"] = url
            Item["goods_name"] = goods_name
            yield Item
