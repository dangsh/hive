# -*- coding: utf-8 -*-
import scrapy


class XunyingItem(scrapy.Item):
    # 名字
    name = scrapy.Field()
    # 又名
    rename = scrapy.Field()
    # 编剧
    screenwriter = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    star = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 地区
    address = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 时长
    long = scrapy.Field()
    # 豆瓣评分
    douban_score = scrapy.Field()
    IMDB_score = scrapy.Field()
    # 临时存评分
    score = scrapy.Field()
    # 上映时间
    time = scrapy.Field()
    # 介绍
    introduce = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 资源
    source = scrapy.Field()