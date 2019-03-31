# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import json
import random
from scrapy.http.response.html import HtmlResponse
# class IPDownloadMiddleware(object):
#     proxies_url = 'http://webapi.http.zhimacangku.com/getip?num=3&type=2&pro=&city=0&yys=0&port=11&pack=40492&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
#
#
#     def process_request(self,request,spider):
#         request.meta['proxy'] = "http://"+random.choice(self.get_proxy())
#
#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         # 如果返回的response状态不是200，重新生成当前request对象
#         if response.status != 200:
#             proxy = "http://"+random.choice(self.get_proxy())
#             print("this is response ip:" + proxy)
#             # 对当前reque加上代理
#             request.meta['proxy'] = proxy
#             return request
#         return response
#
#     def get_proxy(self):
#         proxies=[]
#         r = requests.get(self.proxies_url)
#         ret = json.loads(r.content)
#         for i in ret["data"]:
#            ip = str(i["ip"])
#            port=str(i["port"])
#         # proxies="".decode("utf-8")+ip+":".decode("utf-8")+port
#            proxies.append(ip+":"+port)
#         print(proxies)
#         return proxies
proxies_get="http://210.5.10.87:53281"
class IPDownloadMiddleware(object):
    proxies_url ='http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='


    def process_request(self,request,spider):
            print("request")
            if not request.meta.has_key("proxy"):
                request.meta['proxy'] = "http://163.204.247.37:9999"
                print("自身ip设置="+request.meta['proxy'])

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        print("response")
        if response.status != 200 :
            # proxy = self.get_proxy()
            proxy="http://111.181.38.236:9999"
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def process_exception(self, request, exception, spider):
        print(request.meta.get("proxy",False))
        print("ip异常")
        proxy = "http://121.232.148.52:9999"
        print("this is response ip:" + proxy)
        # 对当前reque加上代理
        request.meta['proxy'] = proxy
        request.meta['DOWNLOAD_TIMEOUT']=4
        return request
        # proxy = self.get_proxy()
        # print("this is response ip:" + proxy)
        # # 对当前reque加上代理
        # request.meta['proxy'] = proxy
        # return request

    def get_proxy(self):
        p=""

        r = requests.get(self.proxies_url)
        ret = json.loads(r.content)
        for i in ret["data"]:
           ip = str(i["ip"])
           port=str(i["port"])
        # proxies="".decode("utf-8")+ip+":".decode("utf-8")+port
           p="http://"+ip+":"+port
        print("提取ip="+p)
        return p

class UAMiddleware(object):
   #定义一个User-Agent的List
   ua_list = [
   'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)'
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)']
   def process_request(self, request, spider): #对request进行拦截
      ua = random.choice(self.ua_list) #使用random模块，随机在ua_list中选取User-Agent
      request.headers['User-Agent'] = ua #把选取出来的User-Agent赋给request
      print(request.headers['User-Agent']) #打印出request的headers

