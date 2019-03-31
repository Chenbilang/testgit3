# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunaeItem(scrapy.Item):
    spot=scrapy.Field()
    spot_id=scrapy.Field()
    hot=scrapy.Field()
    price=scrapy.Field()
    num=scrapy.Field()
    level=scrapy.Field()
