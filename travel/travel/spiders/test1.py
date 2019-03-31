# -*- coding: utf-8 -*-
import scrapy
import re
from travel.items import TravelItem
from selenium import webdriver
from lxml import etree
import time
#城市详情爬虫
class MafengSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/travel-scenic-spot/mafengwo/10189.html']

    def start_requests(self):
        print("dkjfld")
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse
        )

    def parse(self,response):
        item = TravelItem()
        print("进入parse")
        if (response.status != 301):
            item['province'] = response.xpath("//div[@class='crumb']/div[2]//div//span/a/text()").get()
            print(item['province'])
            province_id = response.xpath("//div[@class='crumb']/div[2]//div//span/a/@href").get()
            # 省标号
            try:
                item['province_id'] = int(re.findall("/(\d*)\.", province_id)[0])
            except:
                print("provinceid异常")
                print(province_id)
                print("type=" + type(re.findall("/(\d*)\.", province_id)[0]))
             # 城市
            item['city'] = response.xpath("//div[@class='crumb']/div[3]//div//span/a/text()").get()
            city_id = response.xpath("//div[@class='crumb']/div[3]//div//span/a/@href").get()
            # 城市标号

            item['city_id'] = int(re.findall("/(\d*)\.", city_id)[0])

            # yield self.parse_spot_list(item,spot_list_url)
            yield item











