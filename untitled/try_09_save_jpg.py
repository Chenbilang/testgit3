# coding=utf-8
import requests

r=requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")
#wb表示以二进制写入，w表示以字符串写入
with open("a.png","wb") as f:
    f.write(r.content)