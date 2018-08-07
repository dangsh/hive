# -*- coding: utf-8 -*-
import scrapy
from huicong_goods_geturl.items import HuicongGoodsGeturlItem
import io
from scrapy.exceptions import CloseSpider
class HggSpider(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = 'hgg'
    count = 0
    i = 0

    def start_requests(self):
        with io.open('save.txt') as f:
            stamp = f.read()
        while True:
            stamp2 = str(int(stamp) + self.i)
            self.i += 1
            url = 'https://b2b.hc360.com/supplyself/' + stamp2 + '.html'
            print(url)
            try:
                yield scrapy.Request(url=url, meta={"stamp": stamp2}, callback=self.parse2)
            except:
                pass

    def parse2(self, response):
        stamp = response.meta["stamp"]
        url = response.url
        if response.status == 404:
            self.count += 1
        if response.status == 200:
            # 如果404连续超过 X 个，停止爬虫
            if self.count >= 200:
                # 将结果写入文件
                f = open('save.txt', 'w+')
                f.write(str(int(stamp) - 205))
                f.close()
                # 爬虫关闭，将stamp写入文件
                raise CloseSpider('强制停止')
            # 有一个200，则将count重置
            self.count = 0
            # 将url放入redis中
            Item = HuicongGoodsGeturlItem()
            Item["url"] = url
            yield Item


