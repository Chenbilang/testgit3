# -*- coding: utf-8 -*-
import scrapy
import json

class IpcSpider(scrapy.Spider):
    name = 'ipc'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']
    # allowed_domains = ['google.com']
    # start_urls = ['https://www.google.com']

    # def make_requests_from_url(self, url):
    #     return scrapy.Request(url=url, meta={"proxy":"http://118.24.89.12:1080"}, callback=self.parse, dont_filter=False)
    def parse(self, response):
        # origin=json.loads(response.text)['origin']
        print(response.text)
        yield scrapy.Request(
            'http://httpbin.org/ip',
            callback=self.parse
        )

