# -*- coding: utf-8 -*-
import scrapy
import requests

class ProxSpider(scrapy.Spider):
    name = 'prox'
    start_urls = ['http://ip.seofangfa.com/']

    Cookie = {
        'HMACCOUNT':'F7E3923DFA408C9B',
        'BAIDUID':'5556EDF7B565494EE60D25C772415F9D'
    }

    def parse(self, response):
        # print(response.text)
        for item in response.xpath('//tbody/tr'):
            ip = item.xpath('td/text()').extract()
            try:
                print(ip[0] , ip[1])
                response = requests.get(ip[0])
                print(response)
            except:
                pass
