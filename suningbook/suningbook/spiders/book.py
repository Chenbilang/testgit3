# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        #大小分类
        item = {}
        div_cate=response.xpath("//div[@class='menu-item']")
        for cate in div_cate:

            item['b_cate']=cate.xpath(".//h3/a/text()").extract_first()
            if item['b_cate'] == "文学艺术".decode("utf-8"):
                b_list=cate.xpath(".//dd//a[position()<=3]")
            else:
                b_list = cate.xpath(".//dd//a")

            # s_cate=[]
            # s_href=[]
            for b in b_list:


                if item['b_cate'] == "音像".decode("utf-8"):
                    item["s_href"] = None
                else:
                    item["s_href"] = b.xpath("./@href").extract_first()
                item["s_cate"]=b.xpath("./text()").extract_first()
                    # s_href.extend(b.xpath("./a[position()<=3]/@href").extract())
                    # s_cate.extend(b.xpath("./a[position()<=3]/text()").extract())

                    # s_href.extend(b.xpath("./a/@href").extract())
                    # s_cate.extend(b.xpath("./a/text()").extract())
            # item["s_href"] =s_href
            # item["s_cate"] =s_cate
                if item["s_href"] is not None:
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta ={"item":item}
                    )

    def parse_book_list(self,response):
        item2={}
        item2=response.meta["item"]
        book_item=response.xpath("//ul[@class='clearfix']//li")
        for b in book_item:
            item2["title"]=b.xpath(".//div[@class='res-info']//a[@class='sellPoint']/text()").get()
            item2["img"]=b.xpath(".//div[@class='res-img']//a/img/@src2").get().replace("//","")
            item2["book_href"]=b.xpath(".//div[@class='res-info']//a[@class='sellPoint']/@href").extract_first()
            item2["book_href"]=item2["book_href"].replace("//","https://")
            if item2["book_href"] is not None:
                yield scrapy.Request(
                    item2["book_href"],
                    callback=self.parse_book_detail,
                    meta={"item2": item2}
                )

    def parse_book_detail(self,response):
        item3={}
        item3=response.meta["item2"]
        item3["book_author"]=response.xpath("//div[@id='proinfoMain']/ul/li[1]/text()").get().strip()
        item3["book_publish"]=response.xpath("//div[@id='proinfoMain']/ul/li[2]/text()").get().strip()
        item3["book_time"]=response.xpath("//div[@id='proinfoMain']/ul/li[3]/span[2]/text()").get()
        yield item3