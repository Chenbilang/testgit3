# coding=utf-8
# 只支持中翻英
import requests
import json
while 1:
   str = raw_input("请输入：")
   headers ={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36'}
   data ={
    'from':'zh',
    'to':'en',
    'query':str,
    'sign':'29979.29979',
    'token':'da10a4289c6c2eaa0bc725baa653903a'
}
   post_url="https://fanyi.baidu.com/basetrans"
   r=requests.post(post_url,data=data,headers=headers)
#print (r.content)
   dict_ret=json.loads(r.content)
   ret=dict_ret["trans"][0]["dst"]
   print ("结果是：".decode("utf-8")+ret)