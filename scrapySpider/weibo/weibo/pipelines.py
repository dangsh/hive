# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class WeiboPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            db='weibo',
            user='root',
            passwd='5801200zxg',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute('insert into weibouser(userid , username) value (%s, %s)',(item['userid'] , item['username']))
            # 提交sql语句
            self.connect.commit()
        except Exception as error:
            pass
        return item
