# -*- coding: utf-8 -*-
import scrapy
import json
import re
#城市详情爬虫
class MafengSpider(scrapy.Spider):
    name = 'yjtest'
    allowed_domains = ['mafengwo.cn']
    start_urls=['http://www.mafengwo.cn/yj/10065/']

    def start_requests(self):

        for i in range(1, 7):
            start_url = self.start_urls[0]+'s-{}-0-0-0-1-0.html'.format(i)
            print start_url
            self.start_urls.append(start_url)
        for j in range(1,5):
            start_url = self.start_urls[0] + 's-0-{}-0-0-1-0.html'.format(j)
            print start_url
            self.start_urls.append(start_url)
        for k in range(1,5):
            start_url = self.start_urls[0] + 's-0-0-{}-0-1-0.html'.format(k)
            print start_url
            self.start_urls.append(start_url)
        for url in self.start_urls:
           yield scrapy.Request(
              url=url,
              callback=self.parse
           )
    def parse(self, response):
        page=re.findall("<span>(\d*)</span>条".decode("utf-8"),response.text)[0]
        print page