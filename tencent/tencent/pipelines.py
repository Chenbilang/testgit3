# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def process_item(self, item, spider):
        item=json.dumps(dict(item),ensure_ascii=False,indent=2)
        print(item)
        return item
