#coding=utf-8
list=[]
def meue():
   print "1.新增学生"
   print "2.显示全部"
   print "3,搜索学生"
def add():
   print "."*10,"新增学生","."*10
   name_str = raw_input("请输入姓名")
   age_str = raw_input("请输入年龄")
   dict={'name':name_str,'age':age_str}
   list.append(dict)
   print "添加成功"
def display():
   print "." * 10, "显示全部", "." * 10
   for dic in list:
      print dic
def search():
   search_name=raw_input("请输入要搜索的学生姓名：")
   for dic in list:
      if dic["name"] == search_name:
         print  "找到了"
         print dic
         break
      else:
         print "没找到"