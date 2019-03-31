# -*- coding: UTF-8 -*-

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

# 调用printinfo函数
printinfo(age=50, name="miki"); #关键字参数顺序不重要

'''
     匿名函数
'''

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)

'''
     局部变量和全局变量
'''

total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;

# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total