# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from xunying_redis.items import XunyingItem
import re


class MoviespiderSpider(RedisCrawlSpider):
    name = 'movieSpider'
    allowed_domains = ['www.xunyingwang.com']

    redis_key = 'movieSpider:start_urls'

    rules = (
        Rule(LinkExtractor(allow='movie\/\?page=\d+'), follow=True),
        Rule(LinkExtractor(allow='movie\/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = XunyingItem()
        # 电影名
        item['name'] = response.xpath('/html/body/div[1]/div/div/div[1]/h1/text()').extract()[0].strip()
        introduces = response.xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[2]/p/text()').extract()
        # 介绍
        item['introduce'] = ''.join(introduces).strip()
        tags = response.xpath('/html/body/div[1]/div/div/div[1]/div[3]/div[2]/a/text()').extract()
        item['tags'] = ''.join(tags)
        # 其他信息
        info = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr')
        kMap = {
            '评分': 'score',
            '编剧': 'screenwriter',
            '主演': 'star',
            '地区': 'address',
            '上映时间': 'time',
            '片长': 'long',
            '类型': 'type',
            '又名': 'rename',
            '导演': 'director',
            '语言': 'language'
        }
        for i in info:
            k = i.xpath('./td[1]/span/text()').extract()[0]
            v = ''.join(i.xpath('./td[2]/a/text() | ./td[2]/text()').extract())
            item[kMap.get(k)] = v.strip().replace('/  显示全部', '')
        # yield item
        pattern = re.compile(r'\d+')
        # 电影id
        id = pattern.search(response.url).group()
        baseUrl = 'http://www.xunyingwang.com/videos/resList/'
        yield scrapy.Request(baseUrl + id, meta={'item': item}, callback=self.getDownload)

    # 获取电影下载链接
    def getDownload(self, response):
        item = response.meta['item']
        trs1 = response.xpath('//*[@id="normalDown"]/div/table/tbody/tr')
        trs2 = response.xpath('//*[@id="sourceDown"]/div/table/tbody/tr')
        source = {}
        if trs1:
            source_1 = []
            for tr in trs1:
                tmp = {}
                _name = tr.xpath('./td[1]/span/text()').extract()[0]
                _href = tr.xpath('./td[2]/div/a/@href').extract()[0]
                tmp['name'] = _name
                tmp['source'] = _href
                if _name == '网盘':
                    _pass = tr.xpath('./td[2]/div/strong/text()').extract()[0]
                    tmp['pass'] = _pass
                else:
                    _title = tr.xpath('./td[2]/div/a/text()').extract()[0]
                    tmp['title'] = _title
                    source_1.append(tmp)
                source['normalDown'] = source_1

        if trs2:
            source_1 = []
            for tr in trs2:
                tmp = {}
                _name = tr.xpath('./td[1]/span/text()').extract()[0]
                _href = tr.xpath('./td[2]/div/a/@href').extract()[0]
                tmp['name'] = _name
                tmp['source'] = _href
                if _name == '网盘':
                    _pass = tr.xpath('./td[2]/div/strong/text()').extract()[0]
                    tmp['pass'] = _pass
                else:
                    _title = tr.xpath('./td[2]/div/a/text()').extract()[0]
                    tmp['title'] = _title
                    source_1.append(tmp)
                source['sourceDown'] = source_1

        item['source'] = str(source)
        yield item