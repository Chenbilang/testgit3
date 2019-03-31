# coding=utf-8

print ([i for i in range(3)])
print (["a" for i in range(3) ])
print (["a" for i in range(3) if i%2==0])
print ({i:i+10 for i in range(10)})
for i in range(1,5):
    print(i)
next_url_list=[]
for i in range(2, 10):
    next_url = 'http://www.mafengwo.cn/mdd/citylist/21536.html?page=' + str(i)
    next_url_list.append(next_url)
for i in range(2,10):
    if len(next_url_list)!=0:
      print(next_url_list[0])
      del next_url_list[0]