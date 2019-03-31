# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelItem(scrapy.Item):
    #省份
    province=scrapy.Field()
    #省标号
    province_id=scrapy.Field()
    #城市
    city=scrapy.Field()
    #城市标号
    city_id=scrapy.Field()
    #城市图片
    city_img=scrapy.Field()
    #景点
    spot=scrapy.Field()
    #景点标号
    spot_id=scrapy.Field()
    #景点url
    spot_url=scrapy.Field()
    #景点总评论人数
    spot_ct=scrapy.Field()
    #景点用时参考
    spot_time=scrapy.Field()
    spot_gd=scrapy.Field()
    spot_bd=scrapy.Field()
    b_city=scrapy.Field()
    b_city_id=scrapy.Field()
    spot_yj_ct=scrapy.Field()
    spot_yj_12=scrapy.Field()
    spot_yj_34=scrapy.Field()
    spot_yj_56 = scrapy.Field()
    spot_yj_78 = scrapy.Field()
    spot_yj_910 = scrapy.Field()
    spot_yj_112 = scrapy.Field()
    spot_yj_hundred = scrapy.Field()
    spot_yj_sthousand = scrapy.Field()
    spot_yj_mthousand = scrapy.Field()
    spot_yj_bthousand = scrapy.Field()
    spot_yj_daytime = scrapy.Field()
    spot_yj_weektime = scrapy.Field()
    spot_yj_twoweektime = scrapy.Field()
    spot_yj_bigtime = scrapy.Field()




