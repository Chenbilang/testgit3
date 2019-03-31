# -*- coding: utf-8 -*-
import scrapy
import re
from travel.items import TravelItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import time
import json
import copy
#景点列表爬虫
class MafengSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/citylist/21536.html?page=1']


    def start_requests(self):
        for i in range(2, 11):
            start_url = 'http://www.mafengwo.cn/mdd/citylist/21536.html?page={}'.format(i)
            self.start_urls.append(start_url)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)



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








