# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    userid = scrapy.Field()
    username = scrapy.Field()
    head_img = scrapy.Field()
    register_time = scrapy.Field()
    birthday = scrapy.Field()
    place = scrapy.Field()
    pass
