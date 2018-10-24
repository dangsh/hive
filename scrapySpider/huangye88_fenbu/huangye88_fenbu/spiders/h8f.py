# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
import pyquery
import datetime

class H8fSpider(RedisCrawlSpider):
    name = 'h8f'
    redis_key = 'hy88_url'

    def parse(self, response):
        """
        目前发现两种情况的页面
        http://yongzhou.huangye88.com/xinxi/946_232725872.html
        http://shannan.huangye88.com/xinxi/9465_232727550.html


        移动站
        http://m.huangye88.com/yiqiyibiao/232631426.html      已被删除
        http://m.huangye88.com/d-zunyi/13451-232631425.html   正常
        """
        cate_name_3 = ''
        cate_name_2 = ''
        price_unit = ''
        update_time = ''
        price = ''
        send_time = ''
        keywords = ''
        com_username = ''
        send_money = ''
        thumb = ''
        title = ''
        offer_num = ''
        detail = ''
        seller = ''
        min_price = ''
        cate_name_1 = ''
        to_area = ''
        fax = ''
        thumb_2 = ''
        brand = ''
        thumb_1 = ''
        attrs_kv = []
        min_amount = ''
        auth = ''
        telephone = ''
        ww = ''
        wechat = ''
        source_url = ''
        com_addr = ''
        qq = ''
        mobile = ''
        com_url = ''
        from_area = ''
        max_price = ''
        com_name = ''

        doc = pyquery.PyQuery(response.text)
        for i in doc('img').items():
            if not i.attr('src'):
                i.remove()
        source_url = response.url
        # try:
        #     title = response.xpath('//div[@class="pro-text"]/h1/text()').extract()[0]
        # except:
        #     pass
        # if not title:
        #     try:
        #         title = response.xpath('//div[@class="topinfo"]/h1/text()').extract()[0]
        #     except:
        #         pass
        # try:
        #     price = response.xpath('//h3[@class="big"]/text()').extract()[0].replace('\xa0', '').replace(u'￥', '')
        # except:
        #     pass
        # if not price:
        #     try:
        #         price = response.xpath('//h3[@class="pirce"]/text()').extract()[0].replace(u'元', '')
        #     except:
        #         pass
        # if price:
        #     min_price = price
        #     max_price = price
        # attr_key = []
        # attr_value = []
        # try:
        #     attr_key = response.xpath('//td[@class="attribute"]/div/text()').extract()
        # except:
        #     pass
        #
        # try:
        #     attr_value = response.xpath('//td[@class="attribute-value"]/div/text()').extract()
        # except:
        #     pass
        #
        # try:
        #     for i in range(len(attr_key)):
        #         k = attr_key[i]
        #         v = attr_value[i]
        #         str = k + '|' + v
        #         attrs_kv.append(str)
        # except:
        #     pass
        # imgs = []
        # try:
        #     imgs = response.xpath('//div[@id="picsUrl"]/a/@big').extract()
        # except:
        #     pass
        # try:
        #     thumb = imgs[0]
        # except:
        #     pass
        # try:
        #     thumb_1 = imgs[1]
        # except:
        #     pass
        # try:
        #     thumb_1 = imgs[2]
        # except:
        #     pass

        # ------------------------------------移动站---------------------------------------
        # 通过这个判断商品信息是否已被删除
        if response.xpath('//section[@class="mianbaoxie"]/span'):
            # 未被删除
            try:
                title = response.xpath('//div[@class="text-desc"]/div/h1/text()').extract()[0]
            except:
                pass
            try:
                price = response.xpath('//ul[@class="no-price"]/li/span/text()').extract()[0]
            except:
                pass
            if not price:
                try:
                    price = response.xpath('//span[@class="price left"]/text()').extract()[0]
                except:
                    pass
            try:
                for i in response.xpath('//div[@class="list-desc h"]/ul/li'):
                    k = i.xpath('label/text()').extract()[0]
                    v = i.xpath('span/text()').extract()[0]
                    str = k + '|' + v
                    attrs_kv.append(str)
            except:
                pass
            imgs = []
            try:
                imgs = response.xpath('//ul[@class="swiper-wrapper"]/li/img/@data-src').extract()
            except:
                pass
            try:
                thumb = imgs[0]
            except:
                pass
            try:
                thumb_1 = imgs[1]
            except:
                pass
            try:
                thumb_1 = imgs[2]
            except:
                pass
            try:
                cate_name_1 = response.xpath('//section[@class="mianbaoxie"]/a[1]/text()').extract()[0]
                cate_name_2 = response.xpath('//section[@class="mianbaoxie"]/a[2]/text()').extract()[0]
                cate_name_3 = response.xpath('//section[@class="mianbaoxie"]/a[3]/text()').extract()[0]
            except:
                pass
            try:
                com_name = response.xpath('//li[@class="last"]/span/a/text()').extract()[0]
                com_url = response.xpath('//li[@class="last"]/span/a/@href').extract()[0]
            except:
                pass
            try:
                for i in response.xpath('//div[@class="list-desc"]/ul/li'):
                    if i.xpath('a'):
                        if u'地区' == i.xpath('a/label/text()').extract()[0]:
                            com_addr = i.xpath('a/span/text()').extract()[0]
            except:
                pass



        _ = {
            'source_url': source_url,
            'title': title,
            'price': price,
            'min_price': min_price,
            'max_price': max_price,
            'price_unit': price_unit,
            'min_amount': min_amount,
            'keywords': keywords,
            'brand': brand,
            'to_area': to_area,
            'from_area': from_area,
            'attrs_kv': attrs_kv,
            'cate_name_1': cate_name_1,
            'cate_name_2': cate_name_2,
            'cate_name_3': cate_name_3,
            'thumb': thumb,
            'thumb_1': thumb_1,
            'thumb_2': thumb_2,
            'detail': detail,
            'com_name': com_name,
            'com_addr': com_addr,
            'seller': seller,
            'telephone': telephone,
            'mobile': mobile,
            'qq': qq,
            'ww': ww,
            'wechat': wechat,
            'fax': fax,
            'com_url': com_url,
            'update_time': datetime.datetime.now().strftime('%Y-%m-%d'),
            'sendtime':'',
            'com_username':'',
            'send_money':'',
            'offer_num':'',
            'auth':''
        }
