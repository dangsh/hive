# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from ali.settings import IPPOOL
import time
import requests
import json

class AliSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class MyproxiesSpiderMiddleware(object):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        # thisip = random.choice(IPPOOL)
        # # ip = "211.159.177.212"
        # # port = "3128"
        # #
        # # response = requests.get('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=f605be9dff0448278c340ee5e6deb0b3&orderno=DX201831487120pKssg&returnType=2&count=1&machineArea=')
        # # response = json.loads(response)
        # # ip = response["RESULT"][0]["ip"]
        # # port = response["RESULT"][0]["port"]
        # # print("this ip is " + ip + ":" + port)
        # print("this is ip:" + thisip["ipaddr"])
        # request.meta["proxy"] = "http://" + thisip["ipaddr"]
        # # request.meta["proxy"] = "http://" + ip + ":" + port
        response = requests.get('http://192.168.8.88:7777')
        print(response.text)

        request.meta["proxy"] = "http://" + response.text