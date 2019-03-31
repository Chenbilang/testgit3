#coding=utf-8
import os
# 打开一个文件
fo=open("foo.txt","w")
#写入内容
fo.write("陈碧浪的python文件")
print "文件名",fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
# 关闭打开的文件
fo.close()

fo=open("foo.txt","r+")
#读取xx字节内容
str=fo.read(12)
print "读取的字符串是：",str

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position

print "再次读取的字符串是：",fo.read(12)
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(9)
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()

test1=open("test1.txt","w+")
test1.close()
# 重命名文件test1.txt到test2.txt。
os.rename("test1.txt","test2.txt")
# 删除文件
os.remove("test2.txt")
# 当前目录下新建目录
os.mkdir("test")
# 改变当前目录
os.chdir("C:/Users/2k/PycharmProjects/untitled/test")
# 显示当前目录
print os.getcwd()
os.chdir("C:/Users/2k/PycharmProjects/untitled")
# 删除目录(需要回归要删除目录之前)
os.rmdir("test")