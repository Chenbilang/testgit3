# coding=utf-8
import requests
import json

class BaiduFanyi:
    def __init__(self,trans_str):
        self.lang_detect_url="https://fanyi.baidu.com/langdetect"
        self.trans_str=trans_str
        self.headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Mobile Safari/537.36'}
        self.trans_url="https://fanyi.baidu.com/basetrans"

    def get_response(self,url,data):
        response=requests.post(url,data=data,headers=self.headers)
        return  json.loads(response.content)

    def get_ret(self,dict_response): #提取翻译结果
        ret=dict_response["trans"][0]["dst"]
        print ("翻译结果是:".decode("utf-8")+ret)

    def run(self): #实现主要逻辑
        #1.获取语言类型
            #1.1 准备post的url地址，post_data
        lang_detect_data={'query':self.trans_str}
            #1.2 发送post请求，获取响应
        lang=self.get_response(self.lang_detect_url,lang_detect_data)["lan"]
            #1.3 提取语言类型
        #2. 准备post数据
        trans_data={"query":self.trans_str,"from":"zh","to":"en"} if lang=="zh" \
            else {"query":self.trans_str,"from":"en","to":"zh"}
        #3.发送请求，获取响应
        dict_response=self.get_response(self.trans_url,trans_data)
        #4.提取翻译结果
        self.get_ret(dict_response)

if __name__=='__main__':
    while 1:
        str = raw_input("请输入：")
        baidu_fanyi=BaiduFanyi(str)
        baidu_fanyi.run()