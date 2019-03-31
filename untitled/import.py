# -*- coding: UTF-8 -*-

# 导入模块
import support

# 现在可以调用模块里包含的函数了
while True:
    support.meue()
    str=input("请输入功能序号：")
    if(str==1):
        support.add()
    elif(str==2):
        support.display()
    elif(str==3):
        support.search()
    elif(str==0):
        exit()
    else:
        print "请输入正确序号"