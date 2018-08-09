import requests
from bs4 import BeautifulSoup
import re


class GetStockList(object):

    def get_html_text(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.text  # html变量存储读取的网页text
        except:
            return ''

    def get_stock_list(self, url):
        html = self.get_html_text(url)
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a')
        stock_list = []
        for i in a:
            try:
                href = i.attrs['href']
                stock_num = str(re.findall(r"[s][hz]\d{6}", href)[0])
                if stock_num:
                    stock_list.append(stock_num)
            except:
                continue
        return stock_list


# encoding = utf-8
import requests
import json
import pandas as pd


class GetStockPrice(object):

    def get_daily_price(self, stock):
        DAY_PRICE_URL = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last'
        url = DAY_PRICE_URL % stock
        columns = ['date', 'open', 'high', 'close', 'low', 'volume', 'chg', 'chg_percent', 'ma5', 'ma10', 'ma20','vma5', 'vma10', 'vma20']
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        text = response.text
        js = json.loads(text)
        if js['record']:
            df = pd.DataFrame(js['record'], columns=columns)  #sqlalchemy
        else:
            df = pd.DataFrame(columns=['date', 'open', 'high', 'close', 'low', 'volume', 'chg', 'chg_percent', \
                                       'ma5', 'ma10', 'ma20','vma5', 'vma10', 'vma20'])
            print('该条记录无数据！')


        try:
            df = df.applymap(lambda x: x.replace(',', ''))
            for col in columns[1:]:
                df[col] = df[col].astype('float32')
            df['stock_code'] = stock
        except:
            pass
        return df

# import pymysql
# if __name__ == '__main__':
#     conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='5801200zxg',db='stock',charset='utf8mb4')
#     cursor = conn.cursor()
#     sql_create_table = "CREATE TABLE stockprice (id int not null auto_increment PRIMARY KEY, date DATE,\
#     open float, high float, close float, low float, \
#     volume float, chg float, chg_percent float, ma5 float,ma10 float, ma20 float, \
#     vma5 float, vma10 float, vma20 float, stock_code VARCHAR(255))"
#     cursor.execute(sql_create_table)
#     #sql_insert = "INSERT INTO stockprice (date, open) VALUES ('20160513', 15.44)"
#     conn.commit()
#     print('创建表格成功！')
#     conn.close()
#     print('关闭连接')

import pymysql
import pandas as pd


class InsertIntoMysql(object):
    def insert_into_mysql(self, conn, df):
        cursor = conn.cursor()
        for indexs in df.index:
            full_sql = "insert into stockprice(stock_code, date, open, high, close, low, volume, chg, chg_percent, ma5, ma10,ma20, vma5, vma10, vma20) \
            values ('{}' , '{}' , '{}' , '{}' , '{}' , '{}','{}' , '{}' , '{}' , '{}' , '{}' , '{}','{}' , '{}' , '{}')"\
                .format ( str(df.loc[indexs, 'stock_code']) , str(df.loc[indexs, 'date']) , float(df.loc[indexs, 'open']) , \
                          float(df.loc[indexs, 'high']) , float(df.loc[indexs, 'close']) ,  float(df.loc[indexs, 'low']) , \
                          float(df.loc[indexs, 'volume']) , float(df.loc[indexs, 'chg']) , float(df.loc[indexs, 'chg_percent']) , \
                          float(df.loc[indexs, 'ma5']) , float(df.loc[indexs, 'ma10']) , float(df.loc[indexs, 'ma20']) ,\
                          float(df.loc[indexs, 'vma5']) , float(df.loc[indexs, 'vma10']) ,  float(df.loc[indexs, 'vma20']) )
            cursor.execute(full_sql)
        conn.commit()
        print('写入成功一只股票数据！')

if __name__ == "__main__":
    gsl = GetStockList()
    result = gsl.get_stock_list("http://quote.eastmoney.com/stocklist.html")
    gsp = GetStockPrice()
    iim = InsertIntoMysql()
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='5801200zxg', db='stock',
                           charset='utf8mb4')
    for i in result:
        result2 = gsp.get_daily_price(i)
        iim.insert_into_mysql(conn , result2)