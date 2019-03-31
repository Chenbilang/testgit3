# coding=utf-8
import requests

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
p={'wd':'陈碧浪'}
url_temp="https://www.baidu.com/s?"
r=requests.get(url_temp,headers=headers,params=p)
print (r.status_code)
print(r.request.url)


