# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from huicong_goods_fenbu.items import HuicongGoodsFenbuItem
import re
import redis
import time
import requests
import json
import datetime
import urllib2
import urllib
import pyquery
from gcpy_utils.upyun import *
from gcpy_utils.spider_utils.async_image_push import image_push
import pymysql

class HgfSpider(RedisCrawlSpider):
    name = 'hgf'
    redis_key = 'goods_url'

    def parse(self, response):
        print(response.url)
        title = ""
        price = ""
        offer_num = ""
        send_time = ""
        send_money = ""
        com_name = ""
        buy_sell_num = ""
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
        if response.xpath('//h1[@class="proTitle"]/text()'):
            try:
                try:
                    title = response.xpath('//h1[@class="proTitle"]/text()').extract()[0]
                except:
                    pass
                try:
                    price = response.xpath('//div[@class="topPriceRig"]/text()').extract()[1]
                except:
                    pass
                if not price:
                    try:
                        price = response.xpath('//div[@class="topPriceRig"]/text()').extract()[0]
                        mprice = price.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').split('-')
                        min_price = mprice[0].strip().replace(u'¥', '')
                        max_price = mprice[1].strip().replace(u'¥', '')
                    except:
                        pass
                if not price:
                    try:
                        price = response.xpath('//div[@class="topPriceRig telBra"]/text()').extract()[0]
                    except:
                        pass
                try:
                    price = price.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
                except:
                    pass
                try:
                    if u'¥' in price:
                        price = price.replace(u'¥', '')
                except:
                    pass
                try:
                    offer_num = response.xpath('//span[@class="supply-numb"]/text()').extract()[0]
                except:
                    pass
                try:
                    for i in response.xpath('//div[@class="item-row-w"]'):
                        row = i.xpath('string(.)')
                        if u'发货期限' in row[0].extract():
                            send_time = i.xpath('text()').extract()[1]
                    send_time = send_time.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
                except:
                    pass
                try:
                    buy_sell_num = response.xpath('//li[@class="line-btm"]/div/a/text()').extract()[0]
                except:
                    pass
                try:
                    com_name = response.xpath('//div[@class="comply-name"]/p/a/text()').extract()[0]
                    for i in response.xpath('//div[@class="item-mmt-txt"]/ul/li'):
                        row = i.xpath('string(.)')
                        if u'所在地区' in row[0].extract():
                            com_addr = i.xpath('div/p/text()').extract()[0]
                        if u'认证信息' in row[0].extract():
                            try:
                                auth = i.xpath('div/a/text()').extract()[0]
                            except:
                                auth = i.xpath('div/text()').extract()[0]
                    com_url = response.xpath('//p[@class="cName"]/a/@href').extract()[0]
                except:
                    pass
                try:
                    mobile = response.xpath('//em[@class="c-red"]/text()').extract()[0][1:]
                    telephone = response.xpath('//div[@class="p tel1"]/em/text()').extract()[0]
                    telephone = telephone[1:].split(' ')[0]
                    if not seller:
                        seller = response.xpath('//div[@class="p name"]/em/text()').extract()[0][1:]
                except:
                    pass
                try:
                    for i in response.xpath('//div[@class="d-vopy  parameter "]/ul/li'):
                        key = i.xpath('span/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t',
                                                                                                              '').replace(
                            ' ', '')[:-1]
                        value = i.xpath('p/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t',
                                                                                                             '').replace(
                            ' ', '')
                        str = key + '|' + value
                        attrs_kv.append(str)
                except:
                    pass
                try:
                    thumb = response.xpath('//ul[@id="thumblist"]/li[1]/div/a/@rel').extract()[0]
                    thumb = re.findall(r"largeimage: '(.*?)'", thumb)[0]
                    thumb_1 = response.xpath('//ul[@id="thumblist"]/li[2]/div/a/@rel').extract()[0]
                    thumb_1 = re.findall(r"largeimage: '(.*?)'", thumb_1)[0]
                    thumb_2 = response.xpath('//ul[@id="thumblist"]/li[3]/div/a/@rel').extract()[0]
                    thumb_2 = re.findall(r"largeimage: '(.*?)'", thumb_2)[0]
                except:
                    pass
                try:
                    json_data = re.findall(r'"supCatClass":(.*?),"supcatId"', response.text)[0]
                    json_data = json.loads(json_data)
                    cate_name_1 = json_data[0]["catName"]
                    cate_name_2 = json_data[1]["catName"]
                    cate_name_3 = json_data[2]["catName"]
                except:
                    pass
            except:
                pass

        ss = response.xpath('//script/text()').extract()
        update_time = ''
        keys = []
        for i in ss:
            text = i
            for j in text.split('var'):
                keys.append(j.strip())
        for i in keys:
            i = i.replace('null', 'None').replace('false', 'False').replace('true', 'True')
            if i:
                try:
                    exec i in locals()
                except  Exception as e:
                    pass
        try:
            com_username = company_username.decode('utf-8')
        except:
            com_username = ''
        try:
            keywords = productWord
        except:
            try:
                keywords = searchVal
            except:
                try:
                    keywords = urllib.unquote(keywordencode).decode('gbk')
                except:
                    keywords = ''
        try:
            keywords = keywords.decode('utf-8')
        except:
            pass
        try:
            update_time = supplyInfoJson['pubDate'].split(' ')[0]
        except:
            update_time = (datetime.datetime.now() - datetime.timedelta(30)).strftime('%Y-%m-%d')
        try:
            brand = supplyInfoJson['brandName']
        except:
            brand = ''
        try:
            brand = brand.decode('utf-8')
        except:
            pass
        try:
            businAttList = supplyInfoJson['businAttList']
        except:
            businAttList = []
        from_area = ''
        if businAttList:
            for i in businAttList:
                if i['attname'] == '产地':
                    from_area = i['attvalue']
                if not brand:
                    if i['attname'] == '品牌':
                        brand = i['attvalue']
        try:
            from_area = from_area.decode('utf-8')
        except:
            pass

        try:
            seller = companyContactor
        except:
            try:
                seller = contactor
            except:
                pass
        try:
            fax = companyJson['fax']
        except:
            fax = ''
        to_area = qq = ww = wechat = ''
        try:
            detail = supplyInfoJson['introduce']
            detail = detail.decode("utf-8")
        except:
            pass
        if  u'质量保证，欢迎咨询洽谈' in detail or not detail:
            my_doc = pyquery.PyQuery(response.text)
            my_doc = my_doc("#introduce")
            detail = my_doc.outer_html()
        if detail:
            try:
                doc = pyquery.PyQuery(detail)
            except:
                pass
            print "start up upyun detail"
            try:
                for i in doc('a').items():
                    if i.attr('href') and 'hc360' in i.attr('href'):
                        i.remove()
            except:
                pass
            try:
                for i in doc('img').items():
                    try:
                        if i.attr('data-ke-src'):
                            i.attr('data-ke-src', '')
                    except:
                        pass
                    src = i.attr('src')
                    try:
                        if 'hc360' not in src or 'no_pic' in src or 'nopic' in src:
                            i.remove()
                            continue
                    except:
                        pass
                    try:
                        if thumb and 'no_pic' in thumb:
                            thumb = src
                        if thumb and 'nopic' in thumb:
                            thumb = src
                    except:
                        pass
                    upyun_pic = ''
                    try:
                        upyun_pic = image_push(response.url , src)
                    except:
                        pass
                    if 'hc360' in upyun_pic:
                        i.remove()
                        continue
                    i.attr('src', upyun_pic)
            except:
                pass

            try:
                for i in doc('img').items():
                    if i.attr('src'):
                        src = i.attr('src')
                        if 'hc360' in src or '//' == src:
                            i.remove()
                        if i.attr('data-ke-src'):
                            i.remove_attr('data-ke-src')
                        if i.attr('data-mce-src'):
                            i.remove_attr('data-mce-src')
                        if i.attr('data-cke-saved-src'):
                            i.remove_attr('data-cke-saved-src')
            except:
                pass
            try:
                for i in doc('*').items():
                    if i.attr('src') and 'hc360' in i.attr('src'):
                        i.attr('src', '')
                    if i.attr('data-tfs-url'):
                        i.attr('data-tfs-url', '')
                    if i.attr('data-url'):
                        i.attr('data-url', '')
            except:
                pass
            detail = doc.outer_html()
            try:
                detail = detail.replace('<div style="overflow:hidden;">', '<div>')
            except:
                pass
        if detail and u'正在加载' in detail:
            detail = ''
        try:
            min_amount = int(
                response.xpath('//tr[@class="item-cur-tab"]/td/text()').extract()[0].split('-')[0].strip())
        except:
            min_amount = 1
        try:
            price = re.search(r'\d+\.?\d+', price).group()
        except:
            price = 0
        if not min_price:
            min_price = price
        if not max_price:
            max_price = price
        if offer_num:
            try:
                res = re.search(r'(\d+)(.+)', offer_num.replace(' ', '')).groups()
                offer_num = res[0]
                if len(res) > 1:
                    price_unit = res[1]
            except:
                pass
        print "start up upyun thumb"
        if thumb:
            thumb = image_push(response.url , thumb)
        if 'hc360' in thumb:
            thumb = ''
        if thumb_1:
            thumb_1 = image_push(response.url , thumb_1)
            if 'hc360' in thumb_1:
                thumb_1 = ''
        if thumb_2:
            thumb_2 = image_push(response.url , thumb_2)
            if 'hc360' in thumb_2:
                thumb_2 = ''


        goods_data = {
            'source_url': response.url,
            'title': title,
            'price': price,
            'offer_num': offer_num,
            'send_time': send_time,
            'send_money': send_money,
            'com_name': com_name,
            'com_addr': com_addr,
            'auth': auth,
            'com_url': com_url,
            'mobile': mobile,
            'telephone': telephone,
            'seller': seller,
            'attrs_kv': attrs_kv,
            'detail': detail,
            'thumb_1': thumb_1,
            'thumb_2': thumb_2,
            'thumb': thumb,
            'cate_name_1': cate_name_1,
            'cate_name_2': cate_name_2,
            'cate_name_3': cate_name_3,
            'update_time': datetime.datetime.now().strftime('%Y-%m-%d'),
            'com_username': com_username,
            'keywords': keywords,
            'min_amount': min_amount,
            'min_price': min_price,
            'max_price': max_price,
            'price_unit': price_unit,
            'brand': brand,
            'to_area': to_area,
            'from_area': from_area,
            'qq': qq,
            'ww': ww,
            'fax': fax,
            'wechat': wechat,
        }

        # 获取企业url判断企业是否已被爬取
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
        # 取出企业的关键词
        reg = 'http://(.*?).b2b.hc360.com'
        com_word = re.findall(reg, com_url)[0]
        print(" ")
        test_com_url = 'http://' + com_word + '.wx.hc360.com/shop/show.html'
        conn = pymysql.connect(
            host='192.168.14.90',
            port=3306,
            user='root',
            passwd='123456',
            db='hc360',
            charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute("select * from com_tmp where url = '{}'".format(test_com_url))
        conn.commit()
        result = cursor.fetchone()
        if not result:
            # 企业没有爬过
            try:
                cursor.execute("in sert into com_tmp (url) v  alues ('{}')".format(test_com_url))
                conn.commit()
            except:
                pass
            cursor.close()
            conn.close()
            # 爬取该企业的信息,并将企业信息放入Item 的 com_data中，与goods_data 一起交给mongoPipe处理
            url_1 = "http://detail.b2b.hc360.com/detail/turbine/template/moblie,vmoblie,getcontact_us.html?username="
            try:
                yield scrapy.Request(url=url_1 + com_word, meta={"goods_data": goods_data, "com_word": com_word},callback=self.parse_company)
            except:
                pass
        else:
            cursor.close()
            conn.close()
            # 企业爬过了
            if goods_data["detail"]:
                Item = HuicongGoodsFenbuItem()
                Item["goods_data"] = goods_data
                Item["com_data"] = ""
                yield Item

    def parse_company(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        print(response.url)
        content_1 = response.text
        try:
            content_1 = json.loads(content_1)
        except:
            content_1 = {}

        address = content_1.get('address', '')
        product = content_1.get('business', '')
        comname = content_1.get('companyName', '')
        com_auth = u'已认证' if content_1.get('isAuth', '').lower() == 'true' else u'未认证'
        contact = content_1.get('name', '')
        conn_peopel_sex = content_1.get('gender', '')
        phone_info = content_1.get('phone')
        fax = ''
        mobile = ''
        tel = ''
        if phone_info:
            for i in phone_info:
                if i['name'] == u'传真':
                    fax = i.get('value', '')
                if i['name'] == u'手机':
                    mobile = i.get('value', '')
                if i['name'] == u'电话1':
                    tel = i.get('value', '')
        conn_peopel_position = content_1.get('position', '')
        if not comname.replace(" ", ""):
            comname = u"个人用户"
        com_data = {
            'address': address,
            'product': product,
            'comname': comname,
            'com_auth': com_auth,
            'contact': contact,
            'conn_peopel_sex': conn_peopel_sex,
            'fax': fax,
            'mobile': mobile,
            'tel': tel,
            'conn_peopel_position': conn_peopel_position,
        }

        com_data["source_url"] = ''
        com_data["comname_short"] = ''
        com_data["comtype"] = ''
        com_data["com_addr1"] = ''
        com_data["ceo"] = ''
        com_data["provinces_and_cities"] = ''
        com_data["regyear"] = ''
        com_data["regcapital"] = ''
        com_data["employ"] = ''
        com_data["main_industry"] = ''
        com_data["main_addr"] = ''
        com_data["user_auth"] = ''
        com_data["new_login"] = ''
        com_data["wechat"] = ''
        com_data["comdesc"] = ''
        com_data["com_pic"] = ''
        com_data["com_pic_upyun"] = ''
        com_data["buy_goods"] = ''
        com_data["rdnum"] = ''
        com_data["busmode"] = ''
        com_data["period"] = ''
        com_data["survey"] = ''
        com_data["regist"] = ''
        com_data["com_status"] = ''
        com_data["bank_type"] = ''
        com_data["bank_num"] = ''
        com_data["bank_people"] = ''
        com_data["brand_name"] = ''
        com_data["customer"] = ''
        com_data["annulsale"] = ''
        com_data["annulexport"] = ''
        com_data["annulimport"] = ''
        com_data["business"] = ''
        com_data["com_area"] = ''
        com_data["monthly_production"] = ''
        com_data["OEM"] = ''
        com_data["zip"] = ''
        com_data["com_tel"] = ''
        com_data["email"] = ''
        com_data["website"] = ''
        com_data["aministration_area"] = ''
        com_data["com_addr2"] = ''
        com_data["qc"] = ''
        com_data["com_location"] = ''
        com_data["com_reg_addr"] = ''
        com_data["business_num"] = ''
        com_data["tax_num"] = ''
        com_data["management_system"] = ''
        com_data["conn_peopel_department"] = ''

        url_2 = 'http://detail.b2b.hc360.com/detail/turbine/template/moblie,vmoblie,getcompany_introduction.html?username='
        try:
            yield scrapy.Request(url=url_2 + com_word,
                                 meta={"goods_data": goods_data, "com_word": com_word, "com_data": com_data},
                                 callback=self.parse_company2)
        except:
            pass

    def parse_company2(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        com_data = response.meta["com_data"]
        print(response.url)
        content_2 = response.text
        try:
            content_2 = json.loads(content_2)
        except:
            content_2 = {}
        basic_info = content_2.get('basicInfo', {})
        comdesc = basic_info.get('companyIntroduce', '')
        imageUrl = basic_info.get('imageUrl', [])
        com_pic_upyun = ""
        com_pic = ""
        if imageUrl:
            com_pic = imageUrl[0].get('companyPicUrl', '')
            if com_pic:
                com_pic_upyun = image_push(response.url , com_pic)
        if 'hc360' in com_pic_upyun:
            com_pic_upyun = ''
        detail_info = content_2.get('detailInfo', {})
        if detail_info:
            if not com_data["address"]:
                com_data["address"] = detail_info.get('address', '')
            regcapital = detail_info.get('capital', '')
            if not com_data["contact"]:
                com_data["contact"] = detail_info.get('contactPeople', '')
            regyear = detail_info.get('createDate', '')
            if not com_data["conn_peopel_sex"]:
                com_data["conn_peopel_sex"] = detail_info.get('gender', '')
            main_industry = detail_info.get('industry', '')
            if not com_data["product"]:
                com_data["product"] = detail_info.get('majorProducts', '')
            busmode = detail_info.get('pattern', '')
            phone_info = detail_info.get('phone', [])
            if phone_info:
                for i in phone_info:
                    if i['name'] == u'传真' and not com_data["fax"]:
                        com_data["fax"] = i.get('value', '')
                    if i['name'] == u'手机' and not com_data["mobile"]:
                        com_data["mobile"] = i.get('value', '')
                    if i['name'] == u'电话1' and not com_data["tel"]:
                        com_data["tel"] = i.get('value', '')
            if not com_data["conn_peopel_position"]:
                com_data["conn_peopel_position"] = detail_info.get('position', '')
            ceo = detail_info.get('representative', '')
        com_data["comdesc"] = comdesc
        com_data["com_pic"] = com_pic
        com_data["com_pic_upyun"] = com_pic_upyun
        com_data["regcapital"] = regcapital
        com_data["regyear"] = regyear
        com_data["main_industry"] = main_industry
        com_data["busmode"] = busmode
        com_data["ceo"] = ceo

        try:
            yield scrapy.Request(url='https://js.hc360.com/b2b/%s/company.html' % (com_word,),
                                 meta={"goods_data": goods_data, "com_word": com_word, "com_data": com_data},
                                 callback=self.parse_company3)
        except:
            pass

    def parse_company3(self, response):
        goods_data = response.meta["goods_data"]
        com_word = response.meta["com_word"]
        com_data = response.meta["com_data"]
        print(response.url)
        content_js = response.text
        doc = pyquery.PyQuery(content_js)
        aa = doc('article.intro-list ul')
        for i in aa('li').items():
            if i('.c-left').text() == u'主营产品或服务' and not com_data["product"]:
                com_data["product"] = i('.c-right').text()
            if i('.c-left').text() == u'主营行业' and not com_data["main_industry"]:
                com_data["main_industry"] = i('.c-right').text()
            if i('.c-left').text() == u'企业类型':
                com_data["comtype"] = i('.c-right').text()
            if i('.c-left').text() == u'经营模式' and not com_data["busmode"]:
                com_data["busmode"] = i('.c-right').text()
            if i('.c-left').text() == u'注册地址':
                com_data["com_reg_addr"] = i('.c-right').text()
            if i('.c-left').text() == u'经营地址' and not com_data["address"]:
                com_data["address"] = i('.c-right').text()
            if i('.c-left').text() == u'公司成立时间' and not com_data["regyear"]:
                com_data["regyear"] = i('.c-right').text()
            if i('.c-left').text() == u'法定代表人/负责人' and not com_data["ceo"]:
                com_data["ceo"] = i('.c-right').text()
            if i('.c-left').text() == u'员工人数':
                com_data["employ"] = i('.c-right').text()
            if i('.c-left').text() == u'年营业额':
                com_data["annulsale"] = i('.c-right').text()
            if i('.c-left').text() == u'经营品牌':
                com_data["brand_name"] = i('.c-right').text()
            if i('.c-left').text() == u'注册资本' and not com_data["regcapital"]:
                com_data["regcapital"] = i('.c-right').text()
            if i('.c-left').text() == u'主要客户群':
                com_data["customer"] = i('.c-right').text()
            if i('.c-left').text() == u'主要市场':
                com_data["main_addr"] = i('.c-right').text()
            if i('.c-left').text() == u'是否提供OEM服务':
                com_data["OEM"] = i('.c-right').text()
            if i('.c-left').text() == u'研发部门人数':
                com_data["rdnum"] = i('.c-right').text()
            if i('.c-left').text() == u'厂房面积':
                com_data["com_area"] = i('.c-right').text()
            if i('.c-left').text() == u'质量控制':
                com_data["qc"] = i('.c-right').text()
            if i('.c-left').text() == u'管理体系认证':
                com_data["management_system"] = i('.c-right').text()
            if i('.c-left').text() == u'认证信息' and not com_data["com_auth"]:
                com_data["com_auth"] = i('.c-right').text()
            if i('.c-left').text() == u'开户银行':
                com_data["bank_type"] = i('.c-right').text()
        if 'null' in com_data["regcapital"]:
            com_data["regcapital"] = u'无需验资'
        com_data["source_url"] = 'http://' + com_word + '.wx.hc360.com/shop/show.html'

        if goods_data["detail"]:
            Item = HuicongGoodsFenbuItem()
            Item["com_data"] = com_data
            Item["goods_data"] = goods_data
            yield Item


