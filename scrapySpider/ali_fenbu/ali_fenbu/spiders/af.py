# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ali_fenbu.items import AliFenbuItem
import json
import datetime
import re
import pyquery
from pymongo import MongoClient
import requests
import urllib2
import urllib
import hashlib
import urlparse
from gcpy_utils.upyun import *

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
        if 'alicdn' not in detail_url:
            detail_url = ""
            try:
                doc = pyquery.PyQuery(response.text)
                detail = doc("#de-description-detail").outer_html()
            except:
                pass
        goods_id = ""
        try:
            reg = " 'catid':'(.*?)',"
            goods_id = re.findall(reg , response.text)[0]
        except:
            pass
        if goods_id:
            conn = MongoClient('mongodb://192.168.14.90:27017/')
            db = conn.ali
            data = db.cate.find_one({'_id':int(goods_id)})
            try:
                if data["level"] == 3:
                    cate_name_1 = data["cate1_name"]
                    cate_name_2 = data["cate2_name"]
                    cate_name_3 = data["cate3_name"]
            except:
                pass
        if not cate_name_1:
            #请求接口得到分类
            rsp = requests.post('http://192.168.14.1:8000/pre_api/' , data={'title':title})
            rsp = json.loads(rsp.text)["data"]
            cate_name_1 = rsp[0]
            cate_name_2 = rsp[1]
            cate_name_3 = rsp[2]

        turn_off = ""
        if u'商品已下架' in response.text:
            turn_off = "off"
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

        goods_data = {
            'source_url' : response.url ,
            'title' : title ,
            'price' : price ,
            'offer_num' : offer_num ,
            'send_time' : send_time ,
            'send_money' : send_money ,
            'com_name' : com_name ,
            'com_addr' : com_addr ,
            'auth': auth ,
            'com_url' : com_url ,
            'mobile': mobile ,
            'telephone': telephone ,
            'seller': seller ,
            'attrs_kv' : attrs_kv ,
            'detail': detail ,
            'thumb_1' : thumb_1 ,
            'thumb_2' : thumb_2 ,
            'thumb' : thumb ,
            'cate_name_1': cate_name_1 ,
            'cate_name_2': cate_name_2 ,
            'cate_name_3': cate_name_3 ,
            'update_time': datetime.datetime.now().strftime('%Y-%m-%d') ,
            'com_username': com_username ,
            'keywords': keywords ,
            'min_amount': min_amount ,
            'min_price': min_price ,
            'max_price': max_price ,
            'price_unit': price_unit ,
            'brand': brand ,
            'to_area': to_area ,
            'from_area': from_area ,
            'qq': qq ,
            'ww': ww ,
            'fax': fax ,
            'wechat': wechat ,
        }
        new_url = com_url.replace("companyinfo.htm" , "contactinfo.htm")
        if not turn_off=="off":
            try:
                yield scrapy.Request(url=new_url , meta={"goods_data": goods_data , "detail_url":detail_url} , callback=self.parse2)
            except:
                pass

    def parse2(self, response):
        goods_data = response.meta["goods_data"]
        detail_url = response.meta["detail_url"]
        try:
            goods_data["seller"] = response.xpath('//a[@class="membername"]/text()').extract()[0]
        except:
            pass
        try:
            for i in response.xpath('//div[@class="contcat-desc"]/dl'):
                row = i.xpath('string(.)')
                row = row[0].extract().replace('\r', '').replace('\n', '').replace('\t','').replace(' ', '').replace(u'\xa0','')
                a , b = row.split(u"：")
                if u'电话' == a:
                    goods_data["telephone"] = b
                if u'移动电话' == a and u'登录'not in b:
                    goods_data["mobile"] = b
                if u'传真' == a:
                    goods_data["fax"] = b
                if u'地址' == a:
                    goods_data["com_addr"] = b
        except:
            pass

        if goods_data["thumb"]:
            try:
                hl = hashlib.md5()
                hl.update(goods_data["thumb"].encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = goods_data["thumb"].split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen(goods_data["thumb"]).read()
                goods_data["thumb"] = up_to_upyun("/" + full_name, pic_byte)
            except:
                pass
        if goods_data["thumb_1"]:
            try:
                hl = hashlib.md5()
                hl.update(goods_data["thumb_1"].encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = goods_data["thumb_1"].split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen(goods_data["thumb_1"]).read()
                goods_data["thumb_1"] = up_to_upyun("/" + full_name, pic_byte)
            except:
                pass
        if goods_data["thumb_2"]:
            try:
                hl = hashlib.md5()
                hl.update(goods_data["thumb_2"].encode(encoding='utf-8'))
                src_md5 = hl.hexdigest()  # md5加密的文件名
                # 取出图片后缀
                b = goods_data["thumb_2"].split(".")
                tail = b[-1]
                full_name = src_md5 + "." + tail
                pic_byte = urllib2.urlopen(goods_data["thumb_2"]).read()
                goods_data["thumb_2"] = up_to_upyun("/" + full_name, pic_byte)
            except:
                pass

        com_address = goods_data["com_addr"]
        com_product = ''
        com_comname = goods_data["com_name"]
        com_com_auth = ''
        com_contact = goods_data["seller"]
        com_conn_peopel_sex = ''
        com_fax = goods_data["fax"]
        com_mobile = goods_data["mobile"]
        com_tel = goods_data["telephone"]
        com_conn_peopel_position = ''
        com_source_url = goods_data["com_url"]
        com_comname_short = goods_data["com_name"]
        com_comtype = ''
        com_com_addr1 = ''
        com_ceo = ''
        com_provinces_and_cities = ''
        com_regyear = ''
        com_regcapital = ''
        com_employ = ''
        com_main_industry = ''
        com_main_addr = ''
        com_user_auth = ''
        com_new_login = ''
        com_wechat = ''
        com_comdesc = ''
        com_com_pic = ''
        com_com_pic_upyun = ''
        com_buy_goods = ''
        com_rdnum = ''
        com_busmode = ''
        com_period = ''
        com_survey = ''
        com_regist = ''
        com_com_status = ''
        com_bank_type = ''
        com_bank_num = ''
        com_bank_people = ''
        com_brand_name = ''
        com_customer = ''
        com_annulsale = ''
        com_annulexport = ''
        com_annulimport = ''
        com_business = ''
        com_com_area = ''
        com_monthly_production = ''
        com_OEM = ''
        com_zip = ''
        com_com_tel = ''
        com_email = ''
        com_website = ''
        com_aministration_area = ''
        com_com_addr2 = ''
        com_qc = ''
        com_com_location = ''
        com_com_reg_addr = ''
        com_business_num = ''
        com_tax_num = ''
        com_management_system = ''
        com_conn_peopel_department = ''

        com_data = {
            'address': com_address,
            'product': com_product,
            'comname': com_comname,
            'com_auth': com_com_auth,
            'contact': com_contact,
            'conn_peopel_sex': com_conn_peopel_sex,
            'fax': com_fax,
            'mobile': com_mobile,
            'tel': com_tel,
            'conn_peopel_position': com_conn_peopel_position,
            'source_url': com_source_url,
            'comname_short': com_comname_short,
            'comtype': com_comtype,
            'com_addr1': com_com_addr1,
            'ceo': com_ceo,
            'provinces_and_cities': com_provinces_and_cities,
            'regyear': com_regyear,
            'regcapital': com_regcapital,
            'employ': com_employ,
            'main_industry': com_main_industry,
            'main_addr': com_main_addr,
            'user_auth': com_user_auth,
            'new_login': com_new_login,
            'wechat': com_wechat,
            'comdesc': com_comdesc,
            'com_pic': com_com_pic,
            'com_pic_upyun': com_com_pic_upyun,
            'buy_goods': com_buy_goods,
            'rdnum': com_rdnum,
            'busmode': com_busmode,
            'period': com_period,
            'survey': com_survey,
            'regist': com_regist,
            'com_status': com_com_status,
            'bank_type': com_bank_type,
            'bank_num': com_bank_num,
            'bank_people': com_bank_people,
            'brand_name': com_brand_name,
            'customer': com_customer,
            'annulsale': com_annulsale,
            'annulexport': com_annulexport,
            'annulimport': com_annulimport,
            'business': com_business,
            'com_area': com_com_area,
            'monthly_production': com_monthly_production,
            'OEM': com_OEM,
            'zip': com_zip,
            'com_tel': com_com_tel,
            'email': com_email,
            'website': com_website,
            'aministration_area': com_aministration_area,
            'com_addr2': com_com_addr2,
            'qc': com_qc,
            'com_location': com_com_location,
            'com_reg_addr': com_com_reg_addr,
            'business_num': com_business_num,
            'tax_num': com_tax_num,
            'management_system': com_management_system,
            'conn_peopel_department': com_conn_peopel_department,
        }



        if detail_url:
            try:
                yield scrapy.Request(url=detail_url , meta={"goods_data": goods_data , "com_data" : com_data} , callback=self.parse3)
            except:
                pass
        else:
            if goods_data["detail"]:
                try:
                    doc = pyquery.PyQuery(goods_data["detail"])
                except:
                    pass
                try:
                    for i in doc('img').items():
                        src = i.attr('src')
                        if '?' in src:
                            src = src.split('?')[0]
                        hl = hashlib.md5()
                        hl.update(src.encode(encoding='utf-8'))
                        src_md5 = hl.hexdigest()  # md5加密的文件名
                        # 取出图片后缀
                        b = src.split(".")
                        tail = b[-1]
                        full_name = src_md5 + "." + tail
                        pic_byte = ""
                        new_src = src

                        try:
                            pic_byte = urllib2.urlopen(new_src).read()
                        except:
                            pic_byte = None
                        if not pic_byte:
                            i.remove()
                            continue
                        upyun_pic = up_to_upyun("/" + full_name, pic_byte)
                        # print(upyun_pic)
                        i.attr('src', upyun_pic)
                except:
                    pass
                try:
                    for i in doc('a').items():
                        if 'detail.1688.com' in i.attr('href'):
                            i.attr('href', '')
                    for i in doc('map').items():
                        i.remove()
                except:
                    pass
                goods_data["detail"] = doc.outer_html()
            try:
                yield scrapy.Request(url=goods_data["com_url"] , meta={"goods_data": goods_data , "com_data" : com_data} , callback=self.parse_company)
            except:
                pass




    def parse3(self, response):
        goods_data = response.meta["goods_data"]
        com_data = response.meta["com_data"]
        data = response.text
        try:
            goods_data["detail"] = data[:-3].split('":"')[1]
        except:
            pass
        if goods_data["detail"]:
            try:
                doc = pyquery.PyQuery(goods_data["detail"])
            except:
                pass
            try:
                for i in doc('img').items():
                    src = i.attr('src')
                    if '?' in src:
                        src = src.split('?')[0]
                    if '"' in src:
                        src = src.replace('"' , '').replace('\\' , '')
                    hl = hashlib.md5()
                    hl.update(src.encode(encoding='utf-8'))
                    src_md5 = hl.hexdigest()  # md5加密的文件名
                    # 取出图片后缀
                    b = src.split(".")
                    tail = b[-1]
                    full_name = src_md5 + "." + tail
                    pic_byte = ""
                    new_src = src
                    try:
                        pic_byte = urllib2.urlopen(new_src).read()
                    except:
                        pic_byte = None
                    if not pic_byte:
                        i.remove()
                        continue
                    upyun_pic = up_to_upyun("/" + full_name, pic_byte)
                    # print(upyun_pic)
                    i.attr('src', upyun_pic)
            except:
                pass
            try:
                for i in doc('a').items():
                    if 'detail.1688.com' in i.attr('href'):
                        i.attr('href', '')
                for i in doc('map').items():
                    i.remove()
            except:
                pass
            goods_data["detail"] = doc.outer_html()
        try:
            yield scrapy.Request(url=goods_data["com_url"], meta={"goods_data": goods_data , "com_data":com_data},callback=self.parse_company)
        except:
            pass

    def parse_company(self, response):
        goods_data = response.meta["goods_data"]
        com_data = response.meta["com_data"]
        data = ''
        try:
            data = response.xpath('//span[@class="tb-value-data"]/text()').extract()
        except:
            pass
        if data:
            com_data["regyear"] = data[0]
            com_data["regcapital"] = data[1]
            com_data["com_reg_addr"] = data[3]
            data_list = []
            data_dict = {}
            for i in response.xpath('//div[@id="J_CompanyDetailInfoList"]/div/table/tr/td'):
                data = i.xpath('text()').extract()[0]
                data_list.append(data)
            for i in range(0, len(data_list), 2):
                data_dict[data_list[i]] = data_list[i + 1]
            # print(data_dict)
            try:
                com_data["regcapital"] = data_dict[u"注册资金"]
            except:
                pass
            try:
                com_data["busmode"] = data_dict[u"经营模式"]
            except:
                pass
            try:
                com_data["product"] = data_dict[u"主营产品或服务"]
            except:
                pass
            try:
                com_data["management_system"] = data_dict[u"管理体系认证"]
            except:
                pass
            try:
                com_data["brand_name"] = data_dict[u"品牌名称"]
            except:
                pass
            try:
                com_data["com_area"] = data_dict[u"厂房面积"]
            except:
                pass
            try:
                com_data["employ"] = data_dict[u"员工人数"]
            except:
                pass
            try:
                com_data["monthly_production"] = data_dict[u"月产量"]
            except:
                pass
            try:
                com_data["annulsale"] = data_dict[u"年营业额"]
            except:
                pass
            try:
                com_data["annulexport"] = data_dict[u"年出口额"]
            except:
                pass
            try:
                com_data["comdesc"] = response.xpath('//p[@class="detail-info"]/span/text()').extract()[0]
            except:
                pass
        if not com_data["comname"]:
            try:
                a = response.xpath('//span[@class="name-text"]/text()').extract()[0]
                com_data["comname"] = a.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
                com_data["comname_short"] = com_data["comname"]
            except:
                pass
        test_com_url = 'http://spiderhub.gongchang.com/write_to_online/data_show_onerow?secret=gc7232275&dataset=hc360_company&hkey=' + \
                       com_data["source_url"]
        response = requests.get(test_com_url)
        # print(response.text)
        response = json.loads(response.text)
        # False则该企业未被爬取，True则该企业已被爬取
        print(com_data["source_url"], response["status"])
        if response["status"] != True:
            Item = AliFenbuItem()
            Item["goods_data"] = goods_data
            Item["com_data"] = com_data
            yield Item
        else:
            Item = AliFenbuItem()
            Item["goods_data"] = goods_data
            Item["com_data"] = ""
            yield Item

