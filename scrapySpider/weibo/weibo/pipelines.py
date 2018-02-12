# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from twisted.internet import reactor
import MySQLdb.cursors

class WeiboPipeline(object):
    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host='localhost',
    #         db='weibo',
    #         user='root',
    #         passwd='5801200zxg',
    #         charset='utf8',
    #         use_unicode=True
    #     )
    #     self.cursor = self.connect.cursor()
    #
    # def process_item(self, item, spider):
    #     try:
    #         # 插入数据
    #         self.cursor.execute('insert into weibouser(userid , username) value (%s, %s)',(item['userid'] , item['username']))
    #         # 提交sql语句
    #         self.connect.commit()
    #     except Exception as error:
    #         pass
    #     return item

    def __init__(self, dbpool):
        self.dbpool = dbpool

    # 从配置中获取信息
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入编程异步执行
        # 第一个参数是我们定义的函数
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 错误处理
        query.addErrorback(self.handle_error)

    # 错误处理函数
    def handle_error(self, falure):
        print(falure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = "insert into weibouser(userid , username) value (%s, %s)"
        cursor.execute(insert_sql, (item["userid"],item["username"]))