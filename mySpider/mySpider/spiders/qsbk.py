# -*- coding: utf-8 -*-
import scrapy
import json
from mySpider.items import MyspiderItem
import logging

logger =logging.getLogger(__name__)
class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/text/page/1/']

    def parse(self, response):

        content=response.xpath("//div[@id='content-left']/div")
        print("*" * 100)
        for duanzidiv in content:
            #strip()去除空格
            #xpath()返回的是一个对象需要get提取内容
            #author=duanzidiv.xpath(".//h2/text()").extract_first().strip()
            author=duanzidiv.xpath(".//h2/text()").get().strip()
            #getAll()是得到列表，跟extract一样
            duanziContent=duanzidiv.xpath(".//div[@class='content']//text()").getall()
            duanziContent="".join(duanziContent).strip()
            duanzi={'author':author,'content':duanziContent}
            item=MyspiderItem(author=author,content=duanziContent)
            yield item
            duanziJSON=json.dumps(duanzi,ensure_ascii=False,indent=2)
            logger.warning (duanziJSON)
        print("*"*100)
