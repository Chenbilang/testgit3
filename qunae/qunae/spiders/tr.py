# -*- coding: utf-8 -*-
import scrapy

from qunae.items import QunaeItem
import re
class TrSpider(scrapy.Spider):
    name = 'tr'
    allowed_domains = ['travel.qunar.com']
    start_urls = ["http://piao.qunar.com/ticket/list.htm?keyword='{}'&from=mpl_search_suggest"]

    provinces=['湖南', '湖北', '广东', '广西', '河南', '河北', '山东', '山西', '江苏', '浙江', '江西', '黑龙江', '新疆', '云南', '贵州', '福建', '吉林', '安徽',
     '四川', '西藏', '宁夏', '辽宁', '青海', '甘肃', '陕西', '内蒙古', '台湾', '海南','香港','澳门','天津','上海','重庆','北京']

    def start_requests(self):
        print len(self.provinces)
        for i in self.provinces:
            start_url=self.start_urls[0].format(i)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 dont_filter=True)
    def parse(self, response):
        item=QunaeItem()
        s=response.xpath("//div[@id='search-list']/div")
        for i in s:
            item["spot"]=i.xpath("./@data-sight-name").get()
            item["spot_id"]=i.xpath("./@data-id").get()
            hot=i.xpath(".//div[@class='sight_item_hot']//span[1]/text()").get()
            item["hot"]=hot.split(" ".decode("utf-8"))[-1].strip()
            item["price"]=i.xpath(".//span[@class='sight_item_price']//em/text()").get()
            item["num"]=i.xpath(".//span[@class='hot_num']/text()").get()
            try:
               item["level"]=i.xpath(".//span[@class='level']/text()").get()
            except:
               item["level"]=""
            yield item
