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
    name = 'city2'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/citylist/21536.html']

    def start_requests(self):
        for i in range(2,21):
            start_url='http://www.mafengwo.cn/mdd/citylist/21536.html?page={}'.format(i)
            print start_url
            self.start_urls.append(start_url)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse,
                dont_filter=True)



    def parse(self, response):
        item = TravelItem()
        city_url = response.xpath("//ul[@class='clearfix']//li/div/a")
        for c in city_url:
            # 得到当前页面城市url

            city_list_url = "http://www.mafengwo.cn" + c.xpath("./@href").get()
            # print(city_list_url)
            # 得到城市图片url
            item['city_img'] = c.xpath("./img/@data-original").get()
            # 进入城市详情页
            # yield item
            yield scrapy.Request(
                city_list_url,
                callback=self.parse_city_list,
                meta={  # 传值
                    'item': copy.deepcopy(item)
                }
                ,
                dont_filter=True
            )

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
                    print("爬取城市列表失败，正重新请求")
                    print(response.text)

                    yield scrapy.Request(
                        response.url,
                        callback=self.parse_city_list,
                        dont_filter=True,
                        meta={"item": copy.deepcopy(response.meta['item'])
                              }
                     )
                else:
                    num=len(response.xpath("//div[@class='crumb']//div[@class='item']"))
                    print "num="
                    print num
                    print type(num)
                    if num==4:
                        item["b_city"]=response.xpath("//div[@class='crumb']/div[3]//div//span/a/text()").get()
                        city_id=response.xpath("//div[@class='crumb']/div[3]//div//span/a/@href").get()
                        item["b_city_id"] =int(re.findall("/(\d*)\.", city_id)[0])
                    else:
                        item["b_city"] = ""
                        item["b_city_id"] = 0

                # 城市
                    city_xpath="//div[@class='crumb']/div["+str(num)+"]//div//span/a/text()"
                    city_id_xpath = "//div[@class='crumb']/div[" + str(num) + "]//div//span/a/@href"
                    item['city'] = response.xpath(city_xpath).get()
                    city_id = response.xpath(city_id_xpath).get()
                   # 城市标号
                    item['city_id'] = int(re.findall("/(\d*)\.", city_id)[0])
                # 城市景点列表url
                # spot_list_url = "http://www.mafengwo.cn/jd/" + str(item['city_id']) + "/gonglve.html"
                # yield self.parse_spot_list(item,spot_list_url)
                    spot_list_url = "https://m.mafengwo.cn/jd/" + str(item['city_id']) + "/gonglve.html?page={}&is_ajax=1"
                    # yield self.parse_spot_list(item,spot_list_url)

                    # yield item
                    for i in range(1,21):
                       next_url=spot_list_url.format(i)
                       print("发送请求" + next_url)
                       yield scrapy.Request(
                          next_url,
                          callback=self.parse_spot_list,
                          meta={"item": copy.deepcopy(item)},
                          dont_filter=True,
                          flags=[1],
                       )
    # 景点列表
    def parse_spot_list(self, response):
        if response.text!="":
            print("接受景点列表请求")
            print(response.url)

            item = response.meta['item']
            r = response.body.replace("\\", "")
            try:
                re.findall("<a href=\"(.*?)\" class=\"poi\S*\">", r)
            except:
                print "该景点列表页没加载出来"
                yield scrapy.Request(
                    response.url,
                    callback=self.parse_spot_list,
                    dont_filter=True,
                    meta={"item": copy.deepcopy(response.meta['item'])
                          },
                    flags=[1]
                )

            for i in range(0, len(re.findall("<a href=\"(.*?)\" class=\"poi\S*\">", r))):
                print(i)
                spot_url = re.findall("<a href=\"(.*?)\" class=\"poi\S*\">", r)[i]
                item["spot_url"] = "https://m.mafengwo.cn" + spot_url
                try:
                    item["spot"] = re.findall(r"<p class=\\\"t1\\\" title=\\\"(\S*?)\\\">", response.text)[i].decode(
                        'unicode_escape')
                except:
                    print "spot1方式没找到,采用spot2方式匹配"
                    try:
                        item["spot"] = re.findall(r"<div class=\\\"hd\\\">(\S*?)<\\/div>", response.text)[i].decode(
                        'unicode_escape')
                    except:
                        print("没有找到该页景点")
                # item["spot"] = re.findall("<div class=\"hd\">(.*?)</div>", r)[i]
                item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
                # yield item
                yield scrapy.Request(
                    item["spot_url"],
                    callback=self.parse_spot,
                    meta={"item": copy.deepcopy(item)},
                    flags=[1],
                    dont_filter=True
                )
        else:
            print("没有该页景点")

    def parse_spot(self, response):
        print("进入parse_spot")
        print(response.url)
        item = response.meta['item']

        try:
            item['spot_time'] = response.xpath("//div[@data-jump='costtime']/text()").get()
        except:
            item['spot_time'] = "未知".decode("utf-8")
            print("找不到参考时间")
        finally:
            try:
                spot_ct = response.xpath("//a[@class='commentNum']/strong/text()").get()
                item['spot_ct'] = re.findall("(\d*)条".decode("utf-8"), spot_ct)[0]
            except:
                item['spot_ct'] = 0
                item['spot_gd'] = 0
                item['spot_bd'] = 0

                print("没有评论")
                yield item
            else:

                spot_comment_url = "https://m.mafengwo.cn/poi/comment_" + re.findall("/(\d*)\.html", response.url)[
                    0] + ".html"
                print(spot_comment_url)
                yield scrapy.Request(
                    spot_comment_url,
                    callback=self.parse_spot_comment,
                    meta={"item": copy.deepcopy(item)},
                    flags=[1],
                    dont_filter=True
                )

    def parse_spot_comment(self, response):
        item = response.meta['item']
        item['spot_gd'] = response.xpath("//a[@data-wordid='-13']/i/text()").get()
        item['spot_bd'] = response.xpath("//a[@data-wordid='-11']/i/text()").get()
        yield item















