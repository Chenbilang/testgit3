# coding=utf-8
import requests
import sys
import io
class tieba:
    def __init__(self,tieba_name):
        self.tieba_name=tieba_name
        self.url_temp="https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    def get_url_list(self):
        # url_list=[]
        # for i in range(100):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(100)]
    def get_response(self,url):
        response=requests.get(url,headers=self.headers)
        print (sys.getdefaultencoding()) #c查看默认编码格式
        print (type(response.content.decode("utf-8")))
        return response.content.decode("utf-8")
    def save_html(self,html_str,page_num):
        file_path="{}-第{}页.html".format(self.tieba_name,page_num)
        print (type(file_path.decode("utf-8")))
        with io.open(file_path.decode("utf-8"), "w", encoding="utf-8") as f: #类似f=open(file_path,"w")，会自动close
            f.write(html_str)

    def run(self): #s实现主要逻辑
        #构造url列表
        url_list=self.get_url_list()
        #遍历，发送请求，获取响应
        for url in url_list:
            html_str=self.get_response(url)
            page_num=url_list.index(url)+1
            self.save_html(html_str,page_num)
        #保存

if __name__== '__main__':
    tieba_test=tieba("李毅")
    tieba_test.run()