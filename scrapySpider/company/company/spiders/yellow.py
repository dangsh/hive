# -*- coding: utf-8 -*-
import scrapy
from company.items import CompanyItem

class YellowSpider(scrapy.Spider):
    name = 'yellow'
    
    sum = 0

    start_urls = ['http://b2b.huangye88.com/qiye/ruanjian1720/']

    cookie = {
        'user_trace_token':'20170823200708-9624d434-87fb-11e7-8e7c-5254005c3644',
        'LGUID':'20170823200708-9624dbfd-87fb-11e7-8e7c-5254005c3644 ',
        'index_location_city':'%E5%85%A8%E5%9B%BD',
        'JSESSIONID':'ABAAABAAAIAACBIB27A20589F52DDD944E69CC53E778FA9',
        'TG-TRACK-CODE':'index_code',
        'X_HTTP_TOKEN':'5c26ebb801b5138a9e3541efa53d578f',
        'SEARCH_ID':'739dffd93b144c799698d2940c53b6c1',
        '_gat':'1',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1511162236,1511162245,1511162248,1511166955',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1511166955',
        '_gid':'GA1.2.697960479.1511162230',
        '_ga':'GA1.2.845768630.1503490030',
        'LGSID':'20171120163554-d2b13687-cdcd-11e7-996a-5254005c3644',
        'PRE_UTM':'' ,
        'PRE_HOST':'www.baidu.com',
        'PRE_SITE':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D7awz0WxWjKxQwJ9xplXysE6LwOiAde1dreMKkGLhWzS%26wd%3D%26eqid%3D806a75ed0001a451000000035a128181',
        'PRE_LAND':'https%3A%2F%2Fwww.lagou.com%2F',
        'LGRID':'20171120163554-d2b13811-cdcd-11e7-996a-5254005c3644'
    }

    def parse(self, response):
        #第一次解析 获取省份名字 和 省份Url
        for i in response.xpath('//div[@class="main"]/div[1]/div[@class="ad_list"]/a'):
            firstName = i.xpath("text()").extract()
            firstUrl = i.xpath("@href").extract()
            
            # print(firstName)
            # print(firstUrl)

            oneItem = CompanyItem()
            oneItem["firstName"] = firstName
            oneItem["firstUrl"] = firstUrl
            # yield oneItem
            
            for url in oneItem["firstUrl"]:
                yield scrapy.Request(url=url , cookies=self.cookie , meta = {"firstName" : firstName} , callback=self.parse_url)
        

    def parse_url(self , response):
        #第二次解析 获取公司链接 ，进入下一层
        firstName = response.meta["firstName"]

        #首先计算这个页面有多少页
        # page = response.css('.box .tit2 span em::text').extract()
        # print(page)
        #测试类型转换
        # print(type(int(page[0])))
        # page = int(page[0])//20 + 1
        # print(firstName , page)
        
        #找到公司链接
        for i in response.css('#jubao dl dt h4 a'):
            # companyName = i.xpath('text()').extract()
            companyUrl = i.xpath('@href').extract()
            
            # print(companyName , companyUrl)
            
            yield scrapy.Request(url=companyUrl[0] , cookies=self.cookie , callback=self.parse_url2)

    def parse_url2(self , response):
        #第三次解析 获得公司简介，联系方式url
        
        # a = response.xpath('//p[@class="txt"]/a/@href').extract()
        # print("xxxxxxxxxxxxxxxxxxxxxxxxx" , a)

        jianjieUrl = response.xpath('//ul[@class="meun"]/a[2]/@href').extract()
        # print(jianjieUrl)
        yield scrapy.Request(url=jianjieUrl[0] , cookies=self.cookie , callback=self.parse_url3)

    def parse_url3(self , response):
        #第四次解析 获取公司简介

        hangye = response.xpath('//ul[@class="con-txt"]/li/text()').extract()

        oneItem = CompanyItem()
        oneItem["hangye"] = hangye
        yield oneItem

        # print(hangye)