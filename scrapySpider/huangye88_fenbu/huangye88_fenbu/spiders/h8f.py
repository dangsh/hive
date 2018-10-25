# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
import pyquery
import datetime
from gcpy_utils.spider_utils.async_image_push import shuffle_image_push
import pymysql
from huangye88_fenbu.items import Huangye88FenbuItem
import requests
import json

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
        http://m.huangye88.com/d-nanjing/946-232631428.html   正常2
        http://m.huangye88.com/jiancai/232631442.html         带图片的

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
        #     price = response.xpath('//h3[@class="big"]/text()').extract()[0].replace(u'\xa0', '').replace(u'￥', '')
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
                thumb_2 = imgs[2]
            except:
                pass
            try:
                # cate_name_1 = response.xpath('//section[@class="mianbaoxie"]/a[1]/text()').extract()[0]
                # cate_name_2 = response.xpath('//section[@class="mianbaoxie"]/a[2]/text()').extract()[0]
                # cate_name_3 = response.xpath('//section[@class="mianbaoxie"]/a[3]/text()').extract()[0]
                # 请求接口得到分类
                rsp = requests.post('http://192.168.14.1:8000/pre_api/', data={'title': title})
                rsp = json.loads(rsp.text)["data"]
                cate_name_1 = rsp[0]
                cate_name_2 = rsp[1]
                cate_name_3 = rsp[2]

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
                    if i.xpath('label') and u'联系' == i.xpath('label/text()').extract()[0]:
                        seller = i.xpath('span/text()').extract()[0].replace(u'\xa0', '')
                        mobile = i.xpath('span/a/text()').extract()[0]
            except:
                pass
            doc = pyquery.PyQuery(response.text)
            detail_doc = ''
            try:
                detail_doc = doc('.limit-height')
                for i in detail_doc('img').items():
                    src = i.attr('src')
                    if not src:
                        i.remove()
                    upyun_pic = shuffle_image_push(response.url, src)
                    i.attr('src', upyun_pic)
            except:
                pass
            detail = detail_doc.outer_html()
            detail = detail + u'<p>%s</p><p>联系人：%s</p><p>企业地址：%s</p>' % (com_name, seller, com_addr)
            if thumb:
                try:
                    thumb = shuffle_image_push(response.url , thumb)
                except:
                    pass
            if thumb_1:
                try:
                    thumb_1 = shuffle_image_push(response.url, thumb_1)
                except:
                    pass
            if thumb_2:
                try:
                    thumb_2 = shuffle_image_push(response.url, thumb_2)
                except:
                    pass
            goods_data = {
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
            try:
                yield scrapy.Request(
                    url=com_url,
                    meta={"goods_data": goods_data},
                    callback=self.parse2)
            except:
                pass

    def parse2(self, response):
        goods_data = response.meta["goods_data"]
        com_url = response.xpath('//a[@class="pc"]/@href').extract()[0]
        com_url = com_url.replace('?from=m' , 'company_detail.html')
        goods_data["com_url"] = com_url
        conn = pymysql.connect(
            host='192.168.14.90',
            port=3306,
            user='root',
            passwd='123456',
            db='hy88',
            charset='utf8'
        )
        cursor = conn.cursor()
        cursor.execute("select * from com_url where url = '{}'".format(com_url))
        conn.commit()
        result = cursor.fetchone()
        if not result:
            # 该公司未被爬过
            # try:
            #     cursor.execute("insert into com_url (url) values ('{}')".format(com_url))
            #     conn.commit()
            # except:
            #     pass
            cursor.close()
            conn.close()
            try:
                yield scrapy.Request(
                    url=com_url,
                    meta={"goods_data": goods_data},
                    callback=self.parse_com)
            except:
                pass

        else:
            # 该公司已被爬过
            cursor.close()
            conn.close()
            Item = Huangye88FenbuItem()
            Item["goods_data"] = goods_data
            Item["com_data"] = ""
            yield Item

    def parse_com(self, response):
        goods_data = response.meta["goods_data"]
        # 接下来解析公司的信息
        content = ""
        base_url = ""
        comname = ""
        comname_short = ""
        com_auth = ""
        comtype = ""
        product = ""
        com_addr1 = ""
        ceo = ""
        provinces_and_cities = ""
        comtype = ""
        regyear = ""
        regcapital = ""
        employ = ""
        main_industry = ""
        main_addr = ""
        product = ""
        contact = ""
        user_auth = ""
        new_login = ""
        tel = ""
        mobile = ""
        wechat = ""
        comdesc = ""
        com_pic = ""
        com_pic_upyun = ""
        buy_goods = ""
        main_addr = ""
        rdnum = ""
        busmode = ""
        period = ""
        survey = ""
        regist = ""
        com_status = ""
        bank_type = ""
        bank_num = ""
        bank_people = ""
        brand_name = ""
        customer = ""
        annulsale = ""
        annulexport = ""
        annulimport = ""
        business = ""
        com_area = ""
        monthly_production = ""
        OEM = ""
        zip = ""
        com_tel = ""
        fax = ""
        email = ""
        website = ""
        aministration_area = ""
        com_addr2 = ""
        qc = ""
        address = ""
        com_location = ""
        com_reg_addr = ""
        business_num = ""
        tax_num = ""
        comtype = ""
        regcapital = ""
        regyear = ""
        employ = ""
        management_system = ""
        conn_peopel_sex = ""
        conn_peopel_department = ""
        conn_peopel_position = ""
        try:
            try:
                comname = response.xpath('//ul[@class="l-txt"][1]/li[1]/text()').extract()[0]
                comname_short = response.xpath('//ul[@class="l-txt"][1]/li[2]/text()').extract()[0]
                com_auth = response.xpath('//div[@class="iprz five rzcom"]/text()').extract()[0]
            except:
                pass
            for i in response.xpath('//ul[@class="l-txt"][2]/li'):
                data = i.xpath('text()').extract()[0]
                try:
                    if u'企业类型' in data:
                        comtype = data.split('：')[1]
                    if u'主营产品' in data:
                        product = i.xpath('string(.)').extract()[0]
                        product = product.replace('主营产品：', '')
                    if u'公司地址' in data:
                        com_addr1 = i.xpath('string(.)').extract()[0]
                        com_addr1 = com_addr1.replace('公司地址：', '')
                except:
                    pass
            for i in response.xpath('//ul[@class="con-txt"]/li'):
                data = i.xpath('string(.)').extract()[0]
                try:
                    if u'企业法人' in data:
                        ceo = i.xpath('text()').extract()[0]
                    if u'所在地' in data:
                        provinces_and_cities = i.xpath('text()').extract()[0]
                    if u'企业类型' in data:
                        comtype = i.xpath('text()').extract()[0]
                    if u'成立时间' in data:
                        regyear = i.xpath('text()').extract()[0]
                    if u'注册资金' in data:
                        regcapital = i.xpath('text()').extract()[0]
                    if u'员工人数' in data:
                        employ = i.xpath('text()').extract()[0]
                    if u'主营行业' in data:
                        main_industry = i.xpath('a/text()').extract()[0]
                    if u'主营地区' in data:
                        main_addr = i.xpath('text()').extract()[0]
                    if u'主营产品' in data:
                        product = i.xpath('text()').extract()[0]
                except:
                    pass
            for i in response.xpath('//ul[@class="l-txt none"]/li'):
                data = i.xpath('string(.)').extract()[0]
                if u'联系人' in data:
                    contact = i.xpath('a/text()').extract()[0]
                if u'用户认证' in data:
                    user_auth = i.xpath('string(.)').extract()[0]
                    user_auth = user_auth.replace(u'用户认证：', '')
                if u'最新登录' in data:
                    new_login = i.xpath('text()').extract()[0]
                if u'电话' in data:
                    tel = i.xpath('text()').extract()[0]
                if u'手机' in data:
                    mobile = i.xpath('text()').extract()[0]
                if u'微信号' in data:
                    wechat = i.xpath('text()').extract()[0]
            try:
                for i in response.xpath('//div[@class="r-content"]/p[@class="txt"]'):
                    comdesc = i.xpath('string(.)').extract()[0]
                com_pic = response.xpath('//span[@class="pic"]/img/@src').extract()[0]
            except:
                pass
            for i in response.xpath('//td'):
                data = i.xpath('string(.)').extract()[0]
                try:
                    if u'采购产品' in data:
                        buy_goods = i.xpath('text()').extract()[0]
                    if u'主营地区' in data:
                        main_addr = i.xpath('text()').extract()[0]
                    if u'研发部门人数' in data:
                        rdnum = i.xpath('text()').extract()[0]
                    if u'经营模式' in data:
                        busmode = i.xpath('text()').extract()[0]
                    if u'经营期限' in data:
                        period = i.xpath('text()').extract()[0]
                    if u'最近年检时间' in data:
                        survey = i.xpath('text()').extract()[0]
                    if u'登记机关' in data:
                        regist = i.xpath('text()').extract()[0]
                    if u'企业状态' in data:
                        com_status = i.xpath('text()').extract()[0]
                    if u'开户银行' in data:
                        bank_type = i.xpath('text()').extract()[0]
                    if u'银行账号' in data:
                        bank_num = i.xpath('text()').extract()[0]
                    if u'开户人' in data:
                        bank_people = i.xpath('text()').extract()[0]
                    if u'品牌名称' in data:
                        brand_name = i.xpath('text()').extract()[0]
                    if u'主要客户群' in data:
                        customer = i.xpath('text()').extract()[0]
                    if u'年营业额' in data:
                        annulsale = i.xpath('text()').extract()[0]
                    if u'年营出口额' in data:
                        annulexport = i.xpath('text()').extract()[0]
                    if u'年营进口额' in data:
                        annulimport = i.xpath('text()').extract()[0]
                    if u'经营范围' in data:
                        business = i.xpath('font/text()').extract()[0]
                    if u'厂房面积' in data:
                        com_area = i.xpath('text()').extract()[0]
                    if u'月产量' in data:
                        monthly_production = i.xpath('text()').extract()[0]
                    if u'是否提供OEM' in data:
                        OEM = i.xpath('text()').extract()[0]
                    if u'公司邮编' in data:
                        zip = i.xpath('text()').extract()[0]
                    if u'公司电话' in data:
                        com_tel = i.xpath('text()').extract()[0]
                    if u'公司传真' in data:
                        fax = i.xpath('text()').extract()[0]
                    if u'公司邮箱' in data:
                        email = i.xpath('text()').extract()[0]
                    if u'公司网站' in data:
                        website = i.xpath('text()').extract()[0]
                    if u'行政区域' in data:
                        aministration_area = i.xpath('text()').extract()[0]
                    if u'公司地址' in data:
                        com_addr2 = i.xpath('text()').extract()[0]
                    if u'质量控制' in data:
                        qc = i.xpath('text()').extract()[0]
                    if u'主要经营地点' in data:
                        address = i.xpath('text()').extract()[0]
                    if u'公司所在地' in data:
                        com_location = i.xpath('text()').extract()[0]
                    if u'公司注册地址' in data:
                        com_reg_addr = i.xpath('text()').extract()[0]
                    if u'工商注册号' in data:
                        business_num = i.xpath('text()').extract()[0]
                    if u'税务登记证号' in data:
                        tax_num = i.xpath('text()').extract()[0]
                    if u'企业类型' in data:
                        comtype = i.xpath('text()').extract()[0]
                    if u'注册资金' in data:
                        regcapital = i.xpath('text()').extract()[0]
                    if u'成立时间' in data:
                        regyear = i.xpath('text()').extract()[0]
                    if u'员工人数' in data:
                        employ = i.xpath('text()').extract()[0]
                    if u'管理体系' in data:
                        management_system = i.xpath('text()').extract()[0]
                    if u'联系人性别' in data:
                        conn_peopel_sex = i.xpath('text()').extract()[0]
                    if u'联系人部门' in data:
                        conn_peopel_department = i.xpath('text()').extract()[0]
                    if u'联系人职位' in data:
                        conn_peopel_position = i.xpath('text()').extract()[0]
                except:
                    pass
        except:
            pass
            # 当企业页面为钻石VIP，等特殊页面时
        try:
            if not response.xpath('//div[@class="w-layer"]'):
                try:
                    for i in response.xpath('//div[@class="card-text mt5"]'):
                        try:
                            comname = i.xpath('p[1]/text()').extract()[0]
                        except:
                            pass
                        try:
                            contact = i.xpath('p[2]/text()').extract()[0]
                        except:
                            pass
                        try:
                            mobile = i.xpath('p[3]/text()').extract()[0]
                        except:
                            pass
                        try:
                            tel = i.xpath('p[4]/text()').extract()[0]
                        except:
                            pass
                    com_pic = response.xpath('//div[@class="text-image"]/img/@src').extract()[0]
                    comdesc = response.xpath('//div[@class="pro-text"]/p/text()').extract()[0]
                    if 'none' in com_pic:
                        com_pic = ''
                    for i in response.xpath('//td'):
                        data = i.xpath('string(.)').extract()[0]
                        try:
                            if u'公司主营：' in data:
                                product = i.xpath('text()').extract()[0]
                            if u'主营行业：' in data:
                                main_industry = i.xpath('a/text()').extract()[0]
                            if u'采购产品：' in data:
                                buy_goods = i.xpath('text()').extract()[0]
                            if u'主营地区：' in data:
                                main_addr = i.xpath('text()').extract()[0]
                            if u'研发部门人数：' in data:
                                rdnum = i.xpath('text()').extract()[0]
                            if u'经营模式：' in data:
                                busmode = i.xpath('text()').extract()[0]
                            if u'经营期限：' in data:
                                period = i.xpath('text()').extract()[0]
                            if u'最近年检时间：' in data:
                                survey = i.xpath('text()').extract()[0]
                            if u'登记机关：' in data:
                                regist = i.xpath('text()').extract()[0]
                            if u'企业状态：' in data:
                                com_status = i.xpath('text()').extract()[0]
                            if u'开户银行：' in data:
                                bank_type = i.xpath('text()').extract()[0]
                            if u'银行账号：' in data:
                                bank_num = i.xpath('text()').extract()[0]
                            if u'开户人：' in data:
                                bank_people = i.xpath('text()').extract()[0]
                            if u'品牌名称：' in data:
                                brand_name = i.xpath('text()').extract()[0]
                            if u'主要客户群：' in data:
                                customer = i.xpath('text()').extract()[0]
                            if u'年营业额：' in data:
                                annulsale = i.xpath('text()').extract()[0]
                            if u'年营出口额：' in data:
                                annulexport = i.xpath('text()').extract()[0]
                            if u'年营进口额：' in data:
                                annulimport = i.xpath('text()').extract()[0]
                            if u'经营范围：' in data:
                                business = i.xpath('text()').extract()[0]
                            if u'厂房面积：' in data:
                                com_area = i.xpath('text()').extract()[0]
                            if u'月产量：' in data:
                                monthly_production = i.xpath('text()').extract()[0]
                            if u'是否提供OEM：' in data:
                                OEM = i.xpath('text()').extract()[0]
                            if u'公司邮编：' in data:
                                zip = i.xpath('text()').extract()[0]
                            if u'公司电话：' in data:
                                com_tel = i.xpath('text()').extract()[0]
                            if u'公司传真：' in data:
                                fax = i.xpath('text()').extract()[0]
                            if u'公司邮箱：' in data:
                                email = i.xpath('text()').extract()[0]
                            if u'公司网站：' in data:
                                website = i.xpath('text()').extract()[0]
                            if u'行政区域：' in data:
                                aministration_area = i.xpath('text()').extract()[0]
                            if u'公司地址：' in data:
                                com_addr2 = i.xpath('text()').extract()[0]
                            if u'质量控制：' in data:
                                qc = i.xpath('text()').extract()[0]
                            if u'主要经营地点：' in data:
                                address = i.xpath('text()').extract()[0]
                            if u'公司所在地：' in data:
                                com_location = i.xpath('text()').extract()[0]
                            if u'公司注册地址：' in data:
                                com_reg_addr = i.xpath('text()').extract()[0]
                            if u'工商注册号：' in data:
                                business_num = i.xpath('text()').extract()[0]
                            if u'税务登记证号：' in data:
                                tax_num = i.xpath('text()').extract()[0]
                            if u'企业类型：' in data:
                                comtype = i.xpath('text()').extract()[0]
                            if u'注册资金：' in data:
                                regcapital = i.xpath('text()').extract()[0]
                            if u'成立时间：' in data:
                                regyear = i.xpath('text()').extract()[0]
                            if u'员工人数：' in data:
                                employ = i.xpath('text()').extract()[0]
                            if u'管理体系：' in data:
                                management_system = i.xpath('text()').extract()[0]
                            if u'联系人性别：' in data:
                                conn_peopel_sex = i.xpath('text()').extract()[0]
                            if u'联系人部门：' in data:
                                conn_peopel_department = i.xpath('text()').extract()[0]
                            if u'联系人职位：' in data:
                                conn_peopel_position = i.xpath('text()').extract()[0]
                        except:
                            pass
                except:
                    pass
        except:
            pass
        try:
            if com_pic:
                com_pic_upyun = shuffle_image_push(response.url , com_pic)
        except:
            pass
        com_data = {
            'comname': comname,
            'comname_short': comname_short,
            'com_auth': com_auth,
            'comtype': comtype,
            'product': product,
            'com_addr1': com_addr1,
            'ceo': ceo,
            'provinces_and_cities': provinces_and_cities,
            'regyear': regyear,
            'regcapital': regcapital,
            'employ': employ,
            'main_industry': main_industry,
            'main_addr': main_addr,
            'contact': contact,
            'user_auth': user_auth,
            'new_login': new_login,
            'tel': tel,
            'mobile': mobile,
            'wechat': wechat,
            'comdesc': comdesc,
            'com_pic': com_pic,
            'com_pic_upyun': com_pic_upyun,
            'buy_goods': buy_goods,
            'rdnum': rdnum,
            'busmode': busmode,
            'period': period,
            'survey': survey,
            'regist': regist,
            'com_status': com_status,
            'bank_type': bank_type,
            'bank_num': bank_num,
            'bank_people': bank_people,
            'brand_name': brand_name,
            'customer': customer,
            'annulsale': annulsale,
            'annulexport': annulexport,
            'annulimport': annulimport,
            'business': business,
            'com_area': com_area,
            'monthly_production': monthly_production,
            'OEM': OEM,
            'zip': zip,
            'com_tel': com_tel,
            'fax': fax,
            'email': email,
            'website': website,
            'aministration_area': aministration_area,
            'com_addr2': com_addr2,
            'qc': qc,
            'address': address,
            'com_location': com_location,
            'com_reg_addr': com_reg_addr,
            'business_num': business_num,
            'tax_num': tax_num,
            'regcapital': regcapital,
            'management_system': management_system,
            'conn_peopel_sex': conn_peopel_sex,
            'conn_peopel_department': conn_peopel_department,
            'conn_peopel_position': conn_peopel_position,
        }
        Item = Huangye88FenbuItem()
        Item["goods_data"] = goods_data
        Item["com_data"] = com_data
        yield Item
