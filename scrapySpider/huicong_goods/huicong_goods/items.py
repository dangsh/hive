# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuicongGoodsItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    goods_name = scrapy.Field()
    pass
