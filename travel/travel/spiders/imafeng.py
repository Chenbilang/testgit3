# -*- coding: utf-8 -*-
import scrapy
import re
from travel.items import TravelItem
import copy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support import expected_conditions
import time

class MafengSpider(scrapy.Spider):
    name = 'imafeng'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['https://m.mafengwo.cn/mdd/citylist/21536.html']

    def start_requests(self):
        # FormRequest 是Scrapy发送POST请求的方法
        for i in range(2, 3):
            start_url='https://m.mafengwo.cn/mdd/citylist/21536.html?page='+str(i)
            self.start_urls.append(start_url)
        for url in self.start_urls:
           yield scrapy.Request(
               url,
               callback=self.parse,
               dont_filter=True
           )

    def parse(self, response):
        item = TravelItem()
        # city_url = response.xpath("//ul[@class='clearfix']//li/div/a")

        city_list=response.xpath("//div[@class='cityPoi clearfix']/ul//li")
        for i in city_list:
            city_url=i.xpath("./a/@href").get()
            item["city"]=i.xpath(".//div[@class='name']/p[1]/text()").get()
            item["city_img"]=i.xpath(".//div[@class='photo']/img/@data-original").get()
            item['city_id'] = int(re.findall("/mdd/(\d*)", city_url)[0])
            spot_url_page="https://m.mafengwo.cn/jd/"+str(item["city_id"])+"/gonglve.html?page={}&is_ajax=1"
            for i in range(1,3):
               next_page=spot_url_page.format(i)
               yield scrapy.Request(
                      next_page,
                      callback=self.parse_spot_list,
                      meta={"item": copy.deepcopy(item)},
                      dont_filter=True
                )




    # 爬取景点url
    def parse_spot_list(self, response):
        print("response接受")
        item = response.meta['item']
        r = response.body.replace("\\", "")
        print r
        for i in range(0, len(re.findall("<a href=\"(.*?)\" class=\"poi\S*\">", r))):
            print(i)
            spot_url = re.findall("<a href=\"(.*?)\" class=\"poi\S*\">", r)[i]
            item["spot_url"] = "https://m.mafengwo.cn" + spot_url
            try:

               item["spot"] = re.findall(r"<p class=\\\"t1\\\" title=\\\"(\S*?)\\\">", response.text)[i].decode('unicode_escape')
            except:
               print "spot没找到"
               print response.text
               item["spot"]=re.findall(r"<div class=\\\"hd\\\">(\S*?)<\\/div>", response.text)[i].decode('unicode_escape')
            # item["spot"] = re.findall("<div class=\"hd\">(.*?)</div>", r)[i]
            item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
            yield item
        # if len(self.spot_next_urls) != 0:
        #     next_url = "https://m.mafengwo.cn/jd/" + str(response.meta['item']['city_id']) + "/gonglve.html?page=" + self.spot_next_urls[0] + "&is_ajax=1"
        #     del self.spot_next_urls[0]
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse,
        #         meta={"item": copy.deepcopy(item)}
        #     )










