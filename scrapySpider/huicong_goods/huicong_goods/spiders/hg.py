# -*- coding: utf-8 -*-
import scrapy
import re
from huicong_goods.items import HuicongGoodsItem
import io
import time
from scrapy.exceptions import CloseSpider
import requests
import json
import datetime
import urllib2
import urllib
import pyquery
from gcpy_utils.upyun import *
import hashlib

class HgSpider(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = 'hg'
    count = 0
    i = 0
    def start_requests(self):
        with io.open('save.txt', encoding='utf-8') as f:
            stamp = f.read()
        while True:
            stamp2 = str(int(stamp)+self.i)
            self.i += 1
            url = 'https://b2b.hc360.com/supplyself/'+ stamp2 +'.html'
            print(url)
            try:
                yield scrapy.Request(url=url , meta={"stamp":stamp2} , callback=self.parse2)
            except:
                pass
    def parse2(self, response):
        stamp = response.meta["stamp"]
        url = response.url
        if response.status == 404:
            self.count += 1
        if response.status == 200:
            #如果404连续超过 X 个，停止爬虫
            if self.count >= 3:
                # 将结果写入文件
                f = open('save.txt', 'w+', encoding='utf-8')
                f.write(stamp)
                f.close()
                #爬虫关闭，将stamp写入文件
                raise CloseSpider('强制停止')
            #有一个200，则将count重置
            self.count = 0
            #提取产品信息放入item中
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
                        send_money = response.xpath('//span[@class="i-txt"]/text()')
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
                            key = i.xpath('span/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t','').replace(
                                ' ', '')[:-1]
                            value = i.xpath('p/text()').extract()[0].replace('\r', '').replace('\n', '').replace('\t', '').replace(
                                ' ', '')
                            str = key + '|' + value
                            attrs_kv.append(str)
                    except:
                        pass
                        # try:
                        #     detail = json.loads(data[1:-1])["html"]
                        # except:
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
                # 另一种页面的情况

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
            if detail:
                try:
                    doc = pyquery.PyQuery(detail)
                except:
                    pass
                else:
                    try:
                        for i in doc('img').items():
                            src = i.attr('src')
                            if 'hc360' not in src or 'no_pic' in src:
                                i.remove()
                                continue
                            if thumb and 'no_pic' in thumb:
                                thumb = src
                            hl = hashlib.md5()
                            hl.update(src.encode(encoding='utf-8'))
                            src_md5 = hl.hexdigest()  # md5加密的文件名
                            # 取出图片后缀
                            b = src.split(".")
                            tail = b[-1]
                            full_name = src_md5 + "." + tail
                            pic_byte = urllib2.urlopen("http:" + src).read()
                            upyun_pic = up_to_upyun("/" + full_name, pic_byte)
                            # print(upyun_pic)
                            i.attr('src', upyun_pic)
                    except:
                        pass
                    else:
                        detail = doc.html()
                detail = detail.replace('<div style="overflow:hidden;">', '<div>')
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
            data = {
                'source_url': url,
                'title': title,
                'price': price,
                'offer_num': offer_num,
                'send_time': send_time,
                'send_money': send_money,
                'com_name': com_name,
                # 'buy_sell_num' : buy_sell_num ,
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
                'update_time': update_time,
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

            #获取企业url判断企业是否已被爬取
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
            #取出企业的关键词
            com_word = com_url[7:-15]
            test_com_url = 'http://spiderhub.gongchang.com/write_to_online/data_show_onerow?secret=gc7232275&dataset=hc360_company&hkey=http://' + com_word + '.wx.hc360.com/shop/show.html'
            response = requests.get(test_com_url)
            # print(response.text)
            response = json.loads(response.text)
            #False则该企业未被爬取，True则该企业已被爬取
            print(com_url , response["status"])
            if response["status"] != True:
                #爬取该企业的信息,并将企业信息放入Item 的 com_data中，与goods_data 一起交给mongoPipe处理
                try:
                    yield scrapy.Request(url=url, meta={"data": data}, callback=self.parse_company)
                except:
                    pass
            else:
                Item = HuicongGoodsItem()
                Item["goods_data"] = data
                yield Item



    def parse_company(self, response):
        pass

