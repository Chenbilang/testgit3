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
    name = 'city'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['https://m.mafengwo.cn/mdd/list/pagedata_citylist']
    next_urls=[]
    def start_requests(self):
        # FormRequest 是Scrapy发送POST请求的方法
        for i in range(2,5):
            self.next_urls.append(str(i))

        yield scrapy.FormRequest(
            url=self.start_urls[0],
            formdata={"mddid": "21536", "page": "1"},
            callback=self.parse,
            dont_filter=True
        )


    def parse(self, response):
        item = TravelItem()
        # city_url = response.xpath("//ul[@class='clearfix']//li/div/a")
        print response.text
        r = response.body.replace("\\", "")
        print r

        for i in range(0, len(re.findall("<a href=\"(.*?)\">", r))):
            city_url = re.findall("<a href=\"(.*?)\">", r)[i]
            item["city_img"]=re.findall("data-original=\"(.*?)\"",r)[i]
            # city=re.findall("<p class=\"t1\">(.*?)</p>",r)[i]
            # item["city"]=city.replace("u","\u").decode("utf-8").encode("utf-8")
            item["city"] = re.findall(r"<p class=\\\"t1\\\">(\S*?)<", response.text)[i].decode('unicode_escape')
            # print item["city"]
            item['city_id'] = int(re.findall("/mdd/(\d*)", city_url)[0])
            city_url_page = "https://m.mafengwo.cn/jd/" + item['city_id'] + "/gonglve.html"
            yield scrapy.Request(
                city_url_page,
                callback=self.parse_city_list()
            )
        # for c in city_url:
        #     # 得到当前页面城市url
        #     city_list_url = "http://www.mafengwo.cn" + c.xpath("./@href").get()
        #     # 得到城市图片url
        #
        #     item['city_img'] = c.xpath("./img/@data-original").get()
        #
        #     # 进入城市详情页
        #     yield scrapy.Request(
        #         city_list_url,
        #         callback=self.parse_city_list,
        #         meta={"item":copy.deepcopy(item)},
        #         dont_filter=True
        #     )
        if len(self.next_urls)!=0:
            formdata = {"mddid": "21536", "page":self.next_urls[0] }
            del self.next_urls[0]
            yield scrapy.FormRequest(
                url=self.start_urls[0],
                formdata=formdata,
                callback=self.parse,
                dont_filter=True
            )
        # next_url=response.xpath("//span[@class='pg-current']/text()").get()
        # try :
        #     next_url=int(next_url)+1
        # except:
        #     yield scrapy.Request(
        #         response.url,
        #         callback=self.parse
        #     )
        # if next_url<3:
        #    next_page_url="http://www.mafengwo.cn/mdd/citylist/21536.html?page="+str(next_url)
        #    print(next_page_url)
        #    yield scrapy.Request(
        #       next_page_url,
        #       callback=self.parse,
        #       dont_filter=True
        #    )

    # 爬取城市详情

    def parse_city_list(self, response):
            print("response接受")

            print(response.url)
            item = response.meta['item']
            # 判断是否是城市详情页
            if (response.status != 301):
                # 省份
                item['province'] = response.xpath("//div[@class='crumb']/div[2]//div//span/a/text()").get()
                try:
                   province_id = response.xpath("//div[@class='crumb']/div[2]//div//span/a/@href").get()
                   item['province_id'] = int(re.findall("/(\d*)\.", province_id)[0])
                except:
                    print(response.text)
                    yield scrapy.Request(
                        response.url,
                        callback=self.parse_city_list,
                        dont_filter=True,
                        meta={"item": copy.deepcopy(item)}
                    )
                # 省标号

                # 城市
                item['city'] = response.xpath("//div[@class='crumb']/div[3]//div//span/a/text()").get()
                city_id = response.xpath("//div[@class='crumb']/div[3]//div//span/a/@href").get()
                # 城市标号
                item['city_id'] = int(re.findall("/(\d*)\.", city_id)[0])
                # 城市景点列表url
                spot_list_url = "http://www.mafengwo.cn/jd/" + str(item['city_id']) + "/gonglve.html"
                # yield self.parse_spot_list(item,spot_list_url)
                yield item










