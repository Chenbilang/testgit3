# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import re
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time
import requests
import json
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support import expected_conditions
import time
import scrapy

# class IP1DownloadMiddleware(object):
#     proxies_url ='http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
#     proxy_url='http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
#     def __init__(self):
#         self.proxies_get=self.get_proxies()
#     def process_request(self,request,spider):
#         if len(self.proxies_get)==1:
#             self.proxies_get=self.get_proxies()
#         request.meta['proxy'] = random.choice(self.proxies_get)
#         print("给自身设置ip="+request.meta['proxy'])
#
#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         # 如果返回的response状态不是200，重新生成当前request对象
#
#         if response.status == 301:
#             print("重定向")
#         else:
#             if response.status != 200 :
#                print("ip被封或者网址错误")
#                self.proxies_get.remove(request.meta['proxy'])
#                # 对当前reque加上代理
#                request.meta['proxy'] = random.choice(self.proxies_get)
#                print("更换ip="+request.meta['proxy'])
#                return request
#         return response
#
#     def process_exception(self, request, exception, spider):
#
#         print("ip异常"+request.meta['proxy'])
#         try:
#             self.proxies_get.remove(request.meta['proxy'])
#         finally:
#         # # 对当前reque加上代理
#         # request.meta['proxy'] = random.choice(self.proxies_get)
#         # print(self.proxies_get)
#         # print("异常ip更换="+request.meta['proxy'])
#             return request
#
#     def get_proxies(self):
#         p=[]
#         r = requests.get(self.proxies_url)
#         ret = json.loads(r.content)
#         for i in ret["data"]:
#            ip = str(i["ip"])
#            port=str(i["port"])
#         # proxies="".decode("utf-8")+ip+":".decode("utf-8")+port
#            pr="http://"+ip+":"+port
#            p.append(pr)
#         print("提取ip池=")
#         print(p)
#         return p

class IP2DownloadMiddleware(object):
    proxies_url = 'http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
    def __init__(self):
        print("初始ip池设置")
        self.proxy_get = self.get_proxies()

    def process_request(self,request,spider):
        if not request.meta.has_key("proxy"):
           request.meta['proxy'] =random.choice(self.proxy_get)['proxy']
           # global i  # 再次声明，表示在这里使用的是全局变量，而不是局部变量
           # i = 0  # 这样的话全局变量也会为0
           print("给自身设置ip="+request.meta['proxy'])

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象

        if response.status == 301:
            print("重定向")
        if response.status==302:
            print "302重定向"

        else:
            if response.status != 200 :
               print("ip被封或者网址错误")
               print(response.status)
               request.meta['proxy']= random.choice(self.proxy_get)['proxy']
               print("更换ip="+request.meta['proxy'])
               return request

        return response

    def process_exception(self, request, exception, spider):
        print("ip异常="+request.url)
        if len(self.proxy_get)==1:
            self.proxy_get=self.get_proxies()
        for i in self.proxy_get:
            if i['proxy'] == request.meta["proxy"]:
                i['count'] = i['count'] + 1
                print(self.proxy_get)

            if i['count'] == 30:
                print("移除前")
                print(self.proxy_get)
                self.proxy_get.remove(i)
                print("移除后")
                print(self.proxy_get)
        request.meta["proxy"] = random.choice(self.proxy_get)['proxy']
        return request

    def get_proxies(self):
        p = []
        time.sleep(1)
        r = requests.get(self.proxies_url)
        ret = json.loads(r.content)
        for i in ret["data"]:
            ip = str(i["ip"])
            port = str(i["port"])
            # proxies="".decode("utf-8")+ip+":".decode("utf-8")+port
            pr = "http://" + ip + ":" + port
            pro = {}
            pro['count'] = 0
            pro['proxy'] = pr
            p.append(pro)
        print("提取ip池=")
        print(p)
        return p
        #     proxy_get.remove(request.meta['proxy'])

        # global i  # 再次声明，表示在这里使用的是全局变量，而不是局部变量
        #
        # # print(j)
        #
        #     # # 更换代理
        # try:
        #     print("移除前")
        #     proxy_get.remove(request.meta['proxy'])
        #     print("移除后")
        #     print(proxy_get)
        # finally:
        #     request.meta['proxy'] = random.choice(proxy_get)
        #     i = 0
        # # proxy_get=request.meta['proxy']
        # # print(proxy_get)
        # # i=0
        # # request.meta['proxy']=proxy_get
        # time.sleep(1)
        # print("异常ip更换="+request.meta['proxy'])
        # return request

    # def get_proxies(self):
    #     p=""
    #     time.sleep(1)
    #     r = requests.get(self.proxies_url)
    #     ret = json.loads(r.content)
    #     for i in ret["data"]:
    #        ip = str(i["ip"])
    #        port=str(i["port"])
    #     # proxies="".decode("utf-8")+ip+":".decode("utf-8")+port
    #        p="http://"+ip+":"+port
    #     print("提取ip=")
    #     print(p)
    #     return p



class UAMiddleware(object):
   #定义一个User-Agent的List
   ua_list=[  'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)'
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'
]
   phone_ua_list = [
       "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36",
       "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
       "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36 Edge/15.14900",
       "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",

]
   def process_request(self, request, spider): #对request进行拦截
      #如果是景点详情页请求头改为手机端
      # if re.match("https://m.mafengwo.cn/.*",request.url):
      if request.flags:
         print("手机ui")
         request.headers['User-Agent']=random.choice(self.phone_ua_list)
         print request.headers['User-Agent']
      else:
         print("电脑ui")
         request.headers['User-Agent']= random.choice(self.ua_list) #使用random模块，随机在ua_list中选取User-Agent
         print request.headers['User-Agent']
       #把选取出来的User-Agent赋给request
       #打印出request的headers



# class  MyDownloadMiddleware(object):
#
#
#     def process_request(self, request, spider):
#         # t=test()
#
#         if re.match("http://www.mafengwo.cn/yj/\d*",request.url):
#             print ("进入re")
#             driver = webdriver.Chrome('C:\Google\Chrome\Application\chromedriver.exe')
#              # request._set_url(request.url.split("?")[0])
#             driver.get(request.url)
#             time.sleep(3)
#
#
#             xp="//a[@data-page='"+page+"']"
#             print(xp)
#             try:
#                    xinwei = WebDriverWait(driver, 10).until(
#                        expected_conditions.element_to_be_clickable((By.XPATH, xp)))
#                    xinwei.click()
#                    time.sleep(3)
#                 except:
#                     print("翻页失败")
#             source = driver.page_source
#             response = HtmlResponse(url=request.url, body=source, request=request, encoding="utf-8")
#             return response
#             driver.quit()

class  MyDownloadMiddleware(object):


    def process_request(self, request, spider):
        if re.match("http://www.mafengwo.cn/yj/\d*/s.*",request.url):
            print ("进入re")
            driver = webdriver.Chrome('C:\Google\Chrome\Application\chromedriver.exe')
             # request._set_url(request.url.split("?")[0])
            driver.get(request.url)
            time.sleep(1)
            source = driver.page_source
            response = HtmlResponse(url=request.url, body=source, request=request, encoding="utf-8")
            return response
            driver.quit()








