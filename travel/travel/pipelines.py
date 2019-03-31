# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
class TravelPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'travel',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        # print(json.dumps(dict(item),ensure_ascii=False,indent=2))
        self.cursor.execute(self.sql, (item['province'], item['province_id'], \
                                       item['city'], item['city_id'], item['city_img'], item['spot'], \
                                       item['spot_id'],item['spot_url'],item['spot_ct'],item['spot_time'],\
                                       item['spot_gd'],item['spot_bd']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = '''
                insert into spot2(id,province,province_id,city,city_id,city_img,spot,\
                spot_id,spot_url,spot_ct,spot_time,spot_gd,spot_bd)
                 values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            # self._sql = '''
            #     insert into sopt2(id,province,province_id,city,city_id,city_img,spot,\
            #     spot_id,spot_url)
            #     values(null,%s,%s,%s,%s,%s,%s,%s,%s)
            #  '''
            return self._sql
        return self._sql

    # def process_item(self, item, spider):
    #     item_json=json.dumps(dict(item),ensure_ascii=False,indent=2)
    #     print (item_json)
    #     return item
#使用连接池提高效率
class TwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'travel',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool("pymysql",**dbparams)
        self._sql=None

    @property
    def sql(self):
        if not self._sql:
            self._sql = '''
                insert into s1(id,province,province_id,b_city,b_city_id,city,city_id,city_img,spot,\
                spot_id,spot_url,spot_ct,spot_time,spot_gd,spot_bd)
                 values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            # self._sql = '''
            #     insert into sopt5(id,spot,spot_id,spot_url)
            #      values(null,%s,%s,%s)
            #     '''
            return self._sql
        return self._sql

    def process_item(self, item, spider):

        defer=self.dbpool.runInteraction(self.insert_item,item)
        #添加错误处理函数
        defer.addErback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql, (item['province'], item['province_id'],item['b_city'],item['b_city_id'] ,\
                                       item['city'], item['city_id'], item['city_img'], item['spot'], \
                                       item['spot_id'],item['spot_url'],item['spot_ct'],item['spot_time'],\
                                       item['spot_gd'],item['spot_bd']))
        # cursor.execute(self.sql, (item['spot'], item['spot_id'], item['spot_url']))

    #错误处理
    def handle_error(self,error,item,spider):
        print("="*10+"error"+"*"*10)
        print ("插入数据失败")

class mp(object):
    def process_item(self, item, spider):

       item_json=json.dumps(dict(item),ensure_ascii=False,indent=2)
       print (item_json)
       return item
