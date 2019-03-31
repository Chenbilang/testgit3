# coding=utf-8
import requests

headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
data ={
    'from':'en',
    'to':'zh',
    'query':'hello',
    'transtype':'translang',
    'simple_means_flag':'3',
    'sign':'54706.276099',
    'token':'da10a4289c6c2eaa0bc725baa653903a'
}
post_url="https://fanyi.baidu.com/v2transapi"
r=requests.post(post_url,data=data,headers=headers)
print (r.content)