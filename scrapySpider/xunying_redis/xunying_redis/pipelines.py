# -*- coding: utf-8 -*-

import pymysql
from scrapy.utils.project import get_project_settings
import re

class XunyingPipeline(object):
    # def __init__(self):
    #     # 连接数据库
    #     config = {
    #         'host': get_project_settings().get("MYSQL_HOST"),
    #         'port': get_project_settings().get("MYSQL_PORT"),
    #         'user': get_project_settings().get("MYSQL_USER"),
    #         'password': get_project_settings().get("MYSQL_PASSWD"),
    #         'db': get_project_settings().get("MYSQL_DBNAME"),
    #         'charset': 'utf8',
    #         'cursorclass': pymysql.cursors.DictCursor
    #     }
    #     self.conn = pymysql.connect(**config)
    #     self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        i = dict(item)
        if i.get('long',''):
            com = re.compile(r'\d+')
            long = com.findall(i['long'])[0]
            item['long'] = int(long)
            # i['long'] = int(long)
        if i.get('score', ''):
            sMap = {
                '豆瓣': 'douban_score',
                'IMDB': 'IMDB_score'
            }
            tmp=i['score'].split(' / ')#['豆瓣 6.2','IMDB 6.6']
            if len(tmp):
                for t in tmp:
                    tt=t.split(' ')
                    if tt[1]!='N/A':
                        item[sMap[tt[0]]]=float(tt[1])
                        # i[sMap[tt[0]]]=float(tt[1])
        del item['score']
        # del i['score']
        # if not self.check_item_exists(i.get('name')):
        #     # 如果不存在就插入
        #     self.insert_into_table(i)
        # else:
        #     print('此条数据已存在,不插入')
        return item

    # def insert_into_table(self, i):
    #     sql = "INSERT INTO `movies` (`name`, `rename`, `screenwriter`, `director`, `star`, `type`, `address`, `language`, `long`, `douban_score`, `IMDB_score`, `introduce`, `time`, `tags`,`source`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     insertData = [
    #         i.get('name', ''),
    #         i.get('rename', ''),
    #         i.get('screenwriter', ''),
    #         i.get('director', ''),
    #         i.get('star', ''),
    #         i.get('type', ''),
    #         i.get('address', ''),
    #         i.get('language', ''),
    #         i.get('long', ''),
    #         i.get('douban_score', ''),
    #         i.get('IMDB_score', ''),
    #         i.get('introduce', ''),
    #         i.get('time', ''),
    #         i.get('tags', ''),
    #         i.get('source', '')
    #     ]
    #     res = self.cur.execute(sql, insertData)
    #     if res == 1:
    #         self.conn.commit()
    #         print('成功插入 %d 条数据' % self.cur.rowcount)
    #     else:
    #         print('>>>>>>>>>>>>>>>>>数据没插入<<<<<<<<<<<<<<<<<')
    #
    # # 检查数据是否存在
    # def check_item_exists(self, name):
    #     sql = "SELECT id FROM `movies` WHERE `name` = %s"
    #     self.cur.execute(sql, [name])
    #     count = self.cur.rowcount
    #     print('共查找出 %d 条数据' % count)
    #     if count > 0:
    #         return True
    #     else:
    #         return False
    #
    # # 关闭数据库链接
    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.conn.close()