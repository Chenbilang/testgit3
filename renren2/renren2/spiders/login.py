# -*- coding: utf-8 -*-
import scrapy
import io

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url="http://www.renren.com/PLogin.do"
        data={"email":"13533642854","password":"abc123"}
        request=scrapy.FormRequest(
            url,
            formdata=data,
            callback=self.parse_page
        )
        yield request

    def parse_page(self, response):
        with io.open("renren.html","w",encoding="utf-8") as f:
            f.write(response.text)
        request=scrapy.Request(
            url="http://www.renren.com/969552498/profile",
            callback=self.parse_grzy
        )
        yield request
    def parse_grzy(self,response):
        print(response.text)