# coding=utf-8
import requests
import json
# proxies={'http':'http://httpbin.org/ip'}
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
r=requests.get("http://httpbin.org/ip",headers=headers)
content=json.loads(r.content)
origin=content['origin']
# print (type(origin.encode("utf-8")))
print ("ip地址：".decode("utf-8")+origin)
