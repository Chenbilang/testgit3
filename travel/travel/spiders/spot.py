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
#景点详情爬虫
class MafengSpider(scrapy.Spider):
    name = 'spot'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['https://m.mafengwo.cn/poi/6026847.html']

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            flags=[1]
        )


    def parse(self,response):
        item=TravelItem()

        try:
            item['spot_time'] = response.xpath("//div[@data-jump='costtime']/text()").get()
        except:
            item['spot_time'] = "未知".decode("utf-8")
            print("找不到参考时间")
        finally:
            try:
               spot_ct=response.xpath("//a[@class='commentNum']/strong/text()").get()
               item['spot_ct'] = re.findall("(\d*)条".decode("utf-8"), spot_ct)[0]
            except:
               item['spot_ct'] =0
               item['spot_gd']=0
               item['spot_bd']=0

               print("没有评论")
               yield item
            else:


               spot_comment_url="https://m.mafengwo.cn/poi/comment_"+re.findall("/(\d*)\.html",response.url)[0]+".html"
               print(spot_comment_url)
               yield scrapy.Request(
                  spot_comment_url,
                  callback=self.parse_spot_comment,
                  meta={"item":item},
                  flags = [1]
               )
    def parse_spot_comment(self,response):
        item=response.meta['item']
        item['spot_gd'] = response.xpath("//a[@data-wordid='-13']/i/text()").get()
        item['spot_bd'] = response.xpath("//a[@data-wordid='-11']/i/text()").get()
        yield item










