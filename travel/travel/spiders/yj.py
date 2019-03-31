# -*- coding: utf-8 -*-
import scrapy
import re
from travel.items import TravelItem
from selenium import webdriver
from lxml import etree
import time
import copy
#城市详情爬虫
class MafengSpider(scrapy.Spider):
    name = 'yj'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/citylist/21536.html']

    def start_requests(self):
        for i in range(2, 21):
            start_url = 'http://www.mafengwo.cn/mdd/citylist/21536.html?page={}'.format(i)
            print start_url
            self.start_urls.append(start_url)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse,
                                 dont_filter=True)
    def parse(self, response):
        item = TravelItem()
        city_url = response.xpath("//ul[@class='clearfix']//li/div/a")
        for c in city_url:
            item["city_id"]=int(re.findall("/(\d*)\.", c.xpath("./@href").get())[0]);
            yj_url="http://www.mafengwo.cn/yj/"+item["city_id"]
            yield scrapy.Request(
                yj_url,
                callback=self.parse_yj,
                meta={  # 传值
                    'item': copy.deepcopy(item)
                }
                ,
                dont_filter=True
            )
    def parse_yj(self,response):
        item=response.meta["item"]
        item["spot_yj_ct"]=re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        yj_list=[]
        for i in range(1, 7):
            start_url = item["city_id"] + '/s-{}-0-0-0-1-0.html'.format(i)
            print start_url
            yj_list.append(start_url)
        for j in range(1, 5):
            start_url = item["city_id"] + '/s-0-{}-0-0-1-0.html'.format(j)
            print start_url
            yj_list.append(start_url)
        for k in range(1, 5):
            start_url = item["city_id"] + '/s-0-0-{}-0-1-0.html'.format(k)
            print start_url
            yj_list.append(start_url)
        for url in yj_list:
            yield scrapy.Request(
                url,
                callback=self.parse_yj_list,
                meta={  # 传值
                    'item': copy.deepcopy(item)
                }
                ,
                dont_filter=True
            )
    def parse_yj_list(self,response):
        item=response.meta['item']
        if re.match("http://www.mafengwo.cn/yj/\d*/s-1-0-0-0-1-0.html",response.url):
            item["spot_yj_12"]=re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-2-0-0-0-1-0.html", response.url):
            item["spot_yj_34"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-3-0-0-0-1-0.html", response.url):
            item["spot_yj_56"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-4-0-0-0-1-0.html", response.url):
            item["spot_yj_78"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-5-0-0-0-1-0.html", response.url):
            item["spot_yj_910"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-6-0-0-0-1-0.html", response.url):
            item["spot_yj_112"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-1-0-0-1-0.html", response.url):
            item["spot_yj_hundred"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-2-0-0-1-0.html", response.url):
            item["spot_yj_sthousand"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-3-0-0-1-0.html", response.url):
            item["spot_yj_mthousand"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-4-0-0-1-0.html", response.url):
            item["spot_yj_bthousand"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-0-1-0-1-0.html", response.url):
            item["spot_yj_daytime"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-0-2-0-1-0.html", response.url):
            item["spot_yj_weektime"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-0-3-0-1-0.html", response.url):
            item["spot_yj_twoweektime"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]
        if re.match("http://www.mafengwo.cn/yj/\d*/s-0-0-4-0-1-0.html", response.url):
            item["spot_yj_bigtime"] = re.findall("<span>(\d*)</span>条".decode("utf-8"), response.text)[0]