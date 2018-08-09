# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ali_fenbu.items import AliFenbuItem
import json
import datetime
import re

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



        goods_data = {
            'source_url': response.url,
            'title': title ,
            'price': price ,
            'offer_num': offer_num ,
            'com_name': com_name ,
            'com_url': com_url ,
            'attrs_kv': attrs_kv ,
            'thumb_1': thumb_1 ,
            'thumb_2': thumb_2 ,
            'thumb': thumb ,
            'min_price': min_price ,
            'max_price': max_price ,
        }

        a={'source_url': 'https://detail.1688.com/offer/574932413601.html',
           'title': '曲阜热销小型收获机 四轮带的花生收获机 耐用收获机红薯收获机',
         'price': '2300.00',
           'offer_num': '500台可售',
           'com_name': '曲阜市宏鑫机械厂',
         'com_url': 'https://15554435079.1688.com/page/companyinfo.htm',
         'attrs_kv': ['订货号|HX-TDS-80', '加工定制|是', '货号|HX-TDS-80', '产品类型|全新', '适用对象|薯类,花生', '适用领域|农业', '类型|收获机', '品牌|宏鑫',
                      '型号|HX-TDS-80', '喂入量|1（kg/s） ', '割幅|0.8-1.8', '总损失率|0.1（%） ', '重量|80（kg） ', '生产厂家|曲阜宏鑫机械',
                      '动力类型|柴油', '功率|18（Kw） ', '机器大小|大型', '外型尺寸|可定做（mm） ', '自动化程度|半自动', '售后服务|售后服务 质保两年',
                      '产品规格|手扶带土豆收获机,四轮带土豆收获 机', '主要下游平台|wish,亚马逊,独立站,速卖通,LAZADA,ebay', '主要销售地区|东北亚,东南亚,中东,非洲,欧洲,南美,北美',
                      '有可 授权的自有品牌|是', '是否跨境货源|是', '四轮带的花生收获机|四轮带的花生收获机', '红薯收获机|红薯收获机', '土豆马铃薯收获机|土豆马铃薯收获机'],
         'thumb_1': 'https://cbu01.alicdn.com/img/ibank/2018/702/480/9230084207_1681327681.400x400.jpg',
         'thumb_2': 'https://cbu01.alicdn.com/img/ibank/2018/893/432/9211234398_1681327681.400x400.jpg',
         'thumb': 'https://cbu01.alicdn.com/img/ibank/2018/322/642/9211246223_1681327681.400x400.jpg',
         'min_price': '2300.00',
           'max_price': '2300.00'}







        # goods_data = {
        #     'source_url' : response.url ,
        #     'title' : title ,
        #     'price' : price ,
        #     'offer_num' : offer_num ,
        #     'send_time' : send_time ,
        #     'send_money' : send_money ,
        #     'com_name' : com_name ,
        #     'com_addr' : com_addr ,
        #     'auth': auth ,
        #     'com_url' : com_url ,
        #     'mobile': mobile ,
        #     'telephone': telephone ,
        #     'seller': seller ,
        #     'attrs_kv' : attrs_kv ,
        #     'detail': detail ,
        #     'thumb_1' : thumb_1 ,
        #     'thumb_2' : thumb_2 ,
        #     'thumb' : thumb ,
        #     'cate_name_1': cate_name_1 ,
        #     'cate_name_2': cate_name_2 ,
        #     'cate_name_3': cate_name_3 ,
        #     'update_time': datetime.datetime.now().strftime('%Y-%m-%d') ,
        #     'com_username': com_username ,
        #     'keywords': keywords ,
        #     'min_amount': min_amount ,
        #     'min_price': min_price ,
        #     'max_price': max_price ,
        #     'price_unit': price_unit ,
        #     'brand': brand ,
        #     'to_area': to_area ,
        #     'from_area': from_area ,
        #     'qq': qq ,
        #     'ww': ww ,
        #     'fax': fax ,
        #     'wechat': wechat ,
        # }
        print(goods_data)






