# coding=utf-8
# 使用session登陆
import requests
import io
session=requests.session()
post_url="http://www.renren.com/PLogin.do"
post_data={"email":"13533642854","password":"abc123"}
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
#使用post发送请求将会让cookie也保存其中
session.post(post_url,data=post_data,headers=headers)
r=session.get("http://www.renren.com/969552498",headers=headers)
print(r.status_code)
with io.open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode("utf-8"))