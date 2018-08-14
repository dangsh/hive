# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ali_fenbu.items import AliFenbuItem
import json
import datetime
import re
import pyquery

class AfSpider(RedisCrawlSpider):
    name = 'af'
    redis_key = 'ali_url'

    def parse(self, response):
        title = ""
        price = ""
        offer_num = ""
        send_time = ""
        send_money = ""
        com_name = ""
        com_addr = ""
        auth = ""
        com_url = ""
        mobile = ""
        telephone = ""
        seller = ""
        attrs_kv = []
        detail = ""
        thumb_1 = ""
        thumb_2 = ""
        thumb = ""
        cate_name_1 = ""
        cate_name_2 = ""
        cate_name_3 = ""
        min_price = max_price = 0
        price_unit = ''
        content = data = ''
        com_username = ""
        keywords = ""
        min_amount = ""
        brand = ""
        to_area = ""
        from_area = ""
        qq = ""
        ww = ""
        fax = ""
        wechat = ""
        detail_url = ""
        try:
            title = response.xpath('//h1[@class="d-title"]/text()').extract()[0]
        except:
            pass
        try:
            price = response.xpath('//span[@class="value price-length-4"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value price-length-5"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value price-length-6"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value price-length-7"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value price-length-8"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value price-length-9"]/text()').extract()
            if not price:
                price = response.xpath('//span[@class="value"]/text()').extract()
        except:
            pass
        if u'≥' not in price:
            try:
                price = price[0]
            except:
                pass
        if not price:
            price = ''
        min_price = max_price = price
        try:
            offer_num = response.xpath('//span[@class="total"]/text()').extract()
            if not offer_num:
                for i in response.xpath('//td[@class="count"]/span'):
                    offer_num = i.xpath('string(.)').extract()
        except :
            pass
        if offer_num:
            offer_num = offer_num[0]
            if u'（' in offer_num:
                offer_num = offer_num.replace(u'（','').replace(u'）','')
        if not offer_num:
            offer_num = ''
        try:
            com_name = response.xpath('//div[@class="company-name"]/a/text()').extract()[0]
        except:
            pass
        try:
            com_url = response.xpath('//div[@class="company-name"]/a/@href').extract()[0]
        except:
            pass
        attr_key = []
        attr_value = []
        try:
            attr_key = response.xpath('//td[@class="de-feature"]/text()').extract()
        except:
            pass
        try:
            attr_value = response.xpath('//td[@class="de-value"]/text()').extract()
        except:
            pass
        try:
            for i in range(len(attr_key)):
                k = attr_key[i]
                v = attr_value[i]
                str = k + '|' + v
                attrs_kv.append(str)
        except:
            pass
        imgs = []
        try:
            reg = 'preview":"(.*?)",'
            imgs = re.findall(reg, response.text)
        except:
            pass
        try:
            thumb_1 = imgs[0]
        except:
            pass
        try:
            thumb_2 = imgs[1]
        except:
            pass
        try:
            thumb = imgs[2]
        except:
            pass
        try:
            detail_url = response.xpath('//div[@class="desc-lazyload-container"]/@data-tfs-url').extract()[0]
        except:
            pass
        if not detail_url:
            try:
                detail_url = response.xpath('//div[@id="mod-detail-description"]/@data-mod-config').extract()[0]
                reg = '"contentUrl":"(.*?)"'
                detail_url = re.findall(reg, detail_url)[0]
            except:
                pass

        # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        # print(response.url , detail_url)
        # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        if 'alicdn' not in detail_url:
            doc = pyquery.PyQuery(response.text)
            detail = doc("#de-description-detail").outer_html()
            print(response.url , detail_url , detail)
            # detail = response.xpath('//div[@id="de-description-detail"]')


        # goods_data = {
        #     'source_url': response.url,
        #     'title': title ,
        #     'price': price ,
        #     'offer_num': offer_num ,
        #     'com_name': com_name ,
        #     'com_url': com_url ,
        #     'attrs_kv': attrs_kv ,
        #     'thumb_1': thumb_1 ,
        #     'thumb_2': thumb_2 ,
        #     'thumb': thumb ,
        #     'min_price': min_price ,
        #     'max_price': max_price ,
        # }

    #     goods_data = {
    #         'source_url' : response.url ,
    #         'title' : title ,
    #         'price' : price ,
    #         'offer_num' : offer_num ,
    #         'send_time' : send_time ,
    #         'send_money' : send_money ,
    #         'com_name' : com_name ,
    #         'com_addr' : com_addr ,
    #         'auth': auth ,
    #         'com_url' : com_url ,
    #         'mobile': mobile ,
    #         'telephone': telephone ,
    #         'seller': seller ,
    #         'attrs_kv' : attrs_kv ,
    #         'detail': detail ,
    #         'thumb_1' : thumb_1 ,
    #         'thumb_2' : thumb_2 ,
    #         'thumb' : thumb ,
    #         'cate_name_1': cate_name_1 ,
    #         'cate_name_2': cate_name_2 ,
    #         'cate_name_3': cate_name_3 ,
    #         'update_time': datetime.datetime.now().strftime('%Y-%m-%d') ,
    #         'com_username': com_username ,
    #         'keywords': keywords ,
    #         'min_amount': min_amount ,
    #         'min_price': min_price ,
    #         'max_price': max_price ,
    #         'price_unit': price_unit ,
    #         'brand': brand ,
    #         'to_area': to_area ,
    #         'from_area': from_area ,
    #         'qq': qq ,
    #         'ww': ww ,
    #         'fax': fax ,
    #         'wechat': wechat ,
    #     }
    #     new_url = com_url.replace("companyinfo.htm" , "contactinfo.htm")
    #     try:
    #         yield scrapy.Request(url=new_url , meta={"goods_data": goods_data , "detail_url":detail_url} , callback=self.parse2)
    #     except:
    #         pass
    #
    # def parse2(self, response):
    #     goods_data = response.meta["goods_data"]
    #     detail_url = response.meta["detail_url"]
    #     try:
    #         goods_data["seller"] = response.xpath('//a[@class="membername"]/text()').extract()[0]
    #     except:
    #         pass
    #     try:
    #         for i in response.xpath('//div[@class="contcat-desc"]/dl'):
    #             row = i.xpath('string(.)')
    #             row = row[0].extract().replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '').replace('\xa0','')
    #             # print(row)
    #             a , b = row.split("：")
    #             # print(a)
    #             if u'电话' == a:
    #                 goods_data["telephone"] = i.xpath('dd/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '')
    #             if u'移动电话' == a:
    #                 goods_data["mobile"] = i.xpath('dd/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '')
    #             if u'传真' == a:
    #                 goods_data["fax"] = i.xpath('dd/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '')
    #             if u'地址' == a:
    #                 goods_data["com_addr"] = i.xpath('dd/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '')
    #     except:
    #         pass
    #
    #     # try:
    #     #     detail_url =
    #     # except:
    #     #     pass
    #     # try:
    #     #     yield scrapy.Request(url=new_url , meta={"goods_data": goods_data} , callback=self.parse3)
    #     # except:
    #     #     pass
    #
    # def parse3(self, response):
    #     goods_data = response.meta["goods_data"]

