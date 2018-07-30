# -*- coding: utf-8 -*-
import scrapy
import re
from ali.items import AliItem
from ali.settings import KEY_WORDS
class SunSpider(scrapy.Spider):
    name = 'sun'
    # start_urls = ['']

    def start_requests(self):
        for key_word in KEY_WORDS:
        # key_word = KEY_WORDS[3]
            for i in range(67):
                url = 'https://m.1688.com/gongsi_search/-61.html?keywords='+ key_word +'&sortType=pop&beginPage=' + str(i+1)
                try:
                    yield scrapy.Request(url=url, callback=self.parse2)
                except:
                    pass

    def parse2(self , response):
        response = response.text
        reg = '<li class="li" data-member-id="(.*?)">'
        data = re.findall(reg , response)

        # print(data)
        '''   
        ['b2b-1758000011', 'b2b-33946622896ebe0', 'b2b-3295735784a4049', 'fyxwspc', 'b2b-2156835216',
         'b2b-3009167473ce16b', 'b2b-2834755525df2a5', 'b2b-31932594486d510', 'b2b-331426506880ac7', 'b2b-2527799310',
         'b2b-1917286635', 'b2b-2131282740', 'b2b-2832094374d273d', 'b2b-2924738530e9701', 'b2b-1586888361',
         'b2b-3483477512d47f3', 'b2b-2211133243', 'b2b-345122694413453', 'b2b-325366658958383', 'b2b-2708230949aced8',
         'b2b-2520301186', 'b2b-3551463597bb23d', 'b2b-348535085983d1c', 'b2b-29213739130f09d', 'b2b-3064040776d51c7',
         'b2b-3520145875da217', 'b2b-2253967084', 'b2b-29899548754f808', 'b2b-1116298509', 'b2b-3416996467064ef']
        '''
        Item = AliItem()
        for url in data:
            Item["shopid"] = url
            yield Item
            # for i in range(40):
            #     new_url = 'https://m.1688.com/winport/asyncView?memberId='+ url +'&_async_id=offerlist%3Aoffers&pageIndex=' + str(i+1)
            #     try:
            #         yield scrapy.Request(url=new_url, callback=self.parse3)
            #     except:
            #         pass

    def parse3(self , response):
        response = response.text
        reg = '.html\?offerId=([0-9]*)'
        data = re.findall(reg , response)
        # print(data)
        '''
        ['35676064677', '549726967840', '41194120863', '529491084337', '1267783012', '556450718319', '537147691224', '36963295424']
        ['563612890980', '45341072538', '45318789600', '45279630382', '45252155246', '45274986515', '546054420656', '45340028703']
        '''
        Item = AliItem()
        for i in data:
            Item["userid"] = i
            yield Item