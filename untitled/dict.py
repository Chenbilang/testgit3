#coding=utf-8
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Name']='chenbilang';
del dict['Class'];  # 删除键是'Name'的条目
dict1.clear();  # 清空词典所有条目
del dict1;  # 删除词典
print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];