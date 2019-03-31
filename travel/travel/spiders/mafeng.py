# -*- coding: utf-8 -*-
import scrapy
import re
from travel.items import TravelItem
import copy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support import expected_conditions
import time

class MafengSpider(scrapy.Spider):
    name = 'mafeng'
    allowed_domains = ['mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/citylist/21536.html']
    spot_url_list=[]
    city_url_list=[]
    def start_requests(self):

        for j in range(2, 3):
            page_url="http://www.mafengwo.cn/mdd/citylist/21536.html?page="+str(j)
            self.city_url_list.append(page_url)
        #景点页数
        for j in range(2,6):
            page_url=str(j)
            self.spot_url_list.append(page_url)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse
        )
    def parse(self, response):
        item = TravelItem()
        city_url = response.xpath("//ul[@class='clearfix']//li/div/a")
        for c in city_url:
           # 得到当前页面城市url

           city_list_url="http://www.mafengwo.cn"+c.xpath("./@href").get()
           print(city_list_url)
           # 得到城市图片url
           item['city_img']=c.xpath("./img/@data-original").get()
           #进入城市详情页
           yield scrapy.Request(
               city_list_url,
               callback=self.parse_city_list,
               meta={#传值
                     'item':copy.deepcopy(item),
                     # 禁止301重定向，防止页面跳到景点
                     # 'dont_redirect': True,
                     # 'handle_httpstatus_list': [301]
                     }
           )
        if len(self.city_url_list) != 0:
            next_url = self.city_url_list[0]
            del self.city_url_list[0]
            print("发送请求" + next_url)
            print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        #得到城市页数
        # city_page_str=re.findall("<span class=\"count\">共(\d*)页</span>",response.body)[0]
        # city_page=int(city_page_str)
        #
        # next_url = response.xpath("//span[@class='pg-current']/text()").get()
        # try:
        #     next_url = int(next_url) + 1
        # except:
        #     print("爬取城市列表失败")
        #     print("正重新请求")
        #     yield scrapy.Request(
        #         response.url,
        #         callback=self.parse,
        #         dont_filter = True
        #     )
        # else:
        #     if next_url < 3:
        #        next_page_url = "http://www.mafengwo.cn/mdd/citylist/21536.html?page=" + str(next_url)
        #        print("发送请求")
        #        print(next_page_url)
        #        yield scrapy.Request(
        #            next_page_url,
        #            callback=self.parse,
        #            dont_filter=True
        #        )

        # 进入下一页
        # yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
    #爬取城市详情
    def parse_city_list(self,response):
        print("接受请求")
        print(response.url)
        item=response.meta['item']
        #判断是否是城市详情页
        if (response.status != 301):
            # 省份
            try:
                province_id = response.xpath("//div[@class='crumb']/div[2]//div//span/a/@href").get()
                item['province_id'] = int(re.findall("/(\d*)\.", province_id)[0])
            except:
                print("城市url接受失败")
                print(response.text)
                print("正重新请求")
                yield scrapy.Request(
                    response.url,
                    callback=self.parse_city_list,
                    dont_filter=True,
                    meta={"item": copy.deepcopy(item)}
                )
            else:
                item['province'] = response.xpath("//div[@class='crumb']/div[2]//div//span/a/text()").get()
            # 城市
                item['city'] = response.xpath("//div[@class='crumb']/div[3]//div//span/a/text()").get()
                city_id = response.xpath("//div[@class='crumb']/div[3]//div//span/a/@href").get()
            # 城市标号
                item['city_id'] = int(re.findall("/(\d*)\.", city_id)[0])
            #城市景点列表url

                spot_list_url = "https://m.mafengwo.cn/jd/"+str(item['city_id'])+"/gonglve.html?page=1&is_ajax=1"
            # yield self.parse_spot_list(item,spot_list_url)
                print("发送请求"+spot_list_url)
                # yield item
                yield scrapy.Request(
                   spot_list_url,
                   callback=self.parse_spot_list,
                   meta={"item": copy.deepcopy(item)},
                   flags =[1]
                )
    #景点列表
    def parse_spot_list(self,response):
        print("接受景点列表请求")
        print(response.url)
        item=response.meta['item']
        r = response.body.replace("\\", "")
        for i in range(0, len(re.findall("<a href=\"(.*?)\" class=\"poi\">", r))):
            print(i)
            spot_url=re.findall("<a href=\"(.*?)\" class=\"poi\">", r)[i]
            item["spot_url"] = "https://m.mafengwo.cn"+spot_url
            item["spot"] = re.findall("<a href=\"(.*?)\" class=\"poi\">", r)[i]
            item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
            # yield scrapy.Request(
            #     item["spot_url"],
            #     callback=self.parse_spot,
            #     meta={"item": copy.deepcopy(item)},
            #     flags = [1]
            # )
            yield item

        if len(self.spot_url_list) != 0:
            next_url = "https://m.mafengwo.cn/jd/"+str(item['city_id'])+"/gonglve.html?page="+self.spot_url_list[0]+"&is_ajax=1"
            del self.spot_url_list[0]
            print("发送请求"+next_url)
            print("进入下一页的item")
            print response.meta['item']
            yield scrapy.Request(
                next_url,
                callback=self.parse_spot_list,
                flags = [1],
                meta={"item": copy.deepcopy(response.meta['item'])},
            )
        # spot_list = response.xpath("//div[@class='row row-allScenic']//div[@class='bd']/ul//li//a")
        # for i in spot_list:
        #     item["spot"] = i.xpath("./h3/text()").get()
        #     spot_url = i.xpath("./@href").get()
        #     item["spot_url"] = "http://www.mafengwo.cn" + spot_url
        #     item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
        #     phone_spot_url = "https://m.mafengwo.cn/poi/" + item['spot_id'] + ".html"
        #     yield scrapy.Request(
        #         phone_spot_url,
        #         callback=self.parse_spot,
        #         meta={"item": copy.deepcopy(item)}
        #     )
        # if len(self.page_url_list) != 0:
        #     print("进入pageurl")
        #     next_url = "http://www.mafengwo.cn/jd/10156/gonglve.html?" + self.page_url_list[0]
        #     del self.page_url_list[0]
        #     next_page = response.urljoin(next_url)
        #     print(next_page)
        #     yield scrapy.Request(
        #         next_page,
        #         callback=self.parse_spot_list
        #      )
        # driver2=webdriver.Chrome('C:\Google\Chrome\Application\chromedriver.exe')
        # driver2.get(response.url)
        #
        # for i in range(0,3):
        #     try:
        #         #防止速度太快造成数据丢失
        #         time.sleep(3)
        #         if i!=0:
        #            xinwei = WebDriverWait(driver2, 10).until(
        #             expected_conditions.element_to_be_clickable((By.XPATH, "//a[@class='pi pg-next']")))
        #            xinwei.click()
        #     except:
        #         print("找不到下一页")
        #         break


    def parse_spot(self,response):
        print("进入parse_spot")
        print(response.url)
        item=response.meta['item']
        # try:
        #     item['spot_time'] = response.xpath("//div[@data-jump='costtime']/text()").get()
        # except:
        #     item['spot_time'] = "未知"
        #     print("找不到参考时间")
        #
        # finally:
        #     try:
        #         spot_ct = response.xpath("//a[@class='commentNum']/strong/text()").get()
        #         item['spot_ct'] = re.findall("(\d*)条".decode("utf-8"), spot_ct)[0]
        #     except:
        #         item['spot_ct'] = 0
        #         print("没有评论")
        #     finally:
        #         yield item
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
                    flags = [1]
                )

    def parse_spot_comment(self, response):
        item = response.meta['item']
        item['spot_gd'] = response.xpath("//a[@data-wordid='-13']/i/text()").get()
        item['spot_bd'] = response.xpath("//a[@data-wordid='-11']/i/text()").get()
        yield item









