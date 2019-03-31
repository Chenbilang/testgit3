# coding=utf-8
from lxml import etree

text='''<div><ul>
        <li class="item-1"><a href="link1.html">1 item</a></li>
        <li class="item-2"><a href="link2.html">2 item</a></li>
        <li class="item-1"><a href="link3.html">3 item</a></li>
        <li class="item-2"><a href="link5.html">5 item</a></li>
        <li class="item-1"><a href="link4.html">4 item</a></li>
        </ul></div>
'''
html=etree.HTML(text) #element对象
print(html)
#查看element对象红包含的字符串（会自动修正）
print(etree.tostring(html).decode("utf-8"))

#获取class为item-1的li下a的href
ret1=html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

#获取class为item-1的li下a的文本
ret2=html.xpath("//li[@class='item-1']/a/text()")
print(ret2)
item = {}
#每个li是一条新闻，把url和文本组成字典
for href in ret1:
    item["href"]=href
    item["title"]=ret2[ret1.index(href)]
    print (item)

ret3=html.xpath("//li[@class='item-1']")
for i in ret3:
    item2={}
    item2["title"]=i.xpath("./a/text()")[0] if len(i.xpath("./a/text()"))>0 \
        else None
    item2["href"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/text()")) > 0 \
        else None
    print (item2)