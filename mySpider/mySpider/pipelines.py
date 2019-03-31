# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import io
import logging

logger=logging.getLogger(__name__)
class MyspiderPipeline(object):
    def __init__(self):

        self.fp=io.open('duanzi.json','w',encoding='utf-8')

    def open_spider(self,spider):
        logger.warning("爬虫开始。。")

    def process_item(self, item, spider):
        logger.warning("数据处理。。")
        #dict()将scrapy的数据类型转化成字典
        item_json=json.dumps(dict(item),ensure_ascii=False,indent=2)
        print("write...")
        self.fp.write(item_json+"\n")
        print ("success...")
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束")

# from scrapy.exporters import JsonItemExporter
# import io
# import logging
#
# logger=logging.getLogger(__name__)
#
# class MyspiderPipeline(object):
#     def __init__(self):
#         self.fp=io.open('duanzi.json','wb')
#         self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         logger.warning("爬虫开始。。")
#
#     def process_item(self, item, spider):
#         logger.warning("数据处理。。")
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束")
