# coding=utf-8
# 使用代理访问网站
import requests

proxies={'http':'http://210.5.10.87:53281'}
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
r=requests.get("http://www.baidu.com", proxies=proxies,headers=headers)
print (r.status_code)