# -*- coding: UTF-8 -*-
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
str="/mdd/10189"
if re.match("/(\d*)",str):
    print (True)
str1="热门：1.0"
print str1
str2=re.findall("(.*?)",str1)[0]
print("str2="+str2)
p="1条"
pr=re.findall("(\d*)条",p)[0]
print pr
ip=["115.227.141.231","182.244.168.244","222.185.21.55",
"112.87.90.215", "183.166.163.84","114.106.134.78", "117.68.3.111",
 "106.59.58.206","121.234.54.144","114.221.17.185"]
ip.remove("222.185.21.55")
print(ip)

tr=[{'count': 1, 'proxy': 'http://125.89.40.232:2589'}, {'count': 0, 'proxy': 'http://122.246.102.99:4235'}, {'count': 0, 'proxy': 'http://117.67.126.46:4227'}, {'count': 0, 'proxy': 'http://119.119.107.136:4675'}, {'count': 0, 'proxy': 'http://27.220.52.125:4213'}, {'count': 0, 'proxy': 'http://111.72.152.98:4214'}, {'count': 0, 'proxy': 'http://114.226.101.253:4275'}, {'count': 0, 'proxy': 'http://180.109.39.253:4266'}, {'count': 0, 'proxy': 'http://171.211.102.111:4216'}, {'count': 0, 'proxy': 'http://49.89.110.35:1649'}]
for i in tr:
      if i['count']==1:
         tr.remove(i)
print(tr)
for i in tr:
    if i['proxy']=="http://117.67.126.46:4227":
        i['count']=i['count']+1
print(tr)
url="""
   {has_more: 1,…}
has_more
:
1
html
:
"    <a href=\"\/poi\/829.html\" class=\"poi\">\n <section id="poi_list">↵            <a href="/poi/829.html" class="poi">↵            <dl>↵                <dt><img src="https://b3-q.mafengwo.net/s8/M00/6B/C9/wKgBpVW04GWASRcLAAwS_ra-T5U03.jpeg?imageMogr2%2Fthumbnail%2F%21250x170r%2Fgravity%2FCenter%2Fcrop%2F%21250x170%2Fquality%2F100" width="100%" alt=""/></dt>↵                <dd>↵                    <p class="t1" title="鼓浪屿">鼓浪屿↵                        <span class="tag">推荐</span>                        ↵                    </p>↵                    <p class="t2"></p>↵                    <div class="t3">↵                                                    <strong class="num">12530</strong>条蜂评 ，                            <strong class="num">2667</strong>篇游记提到                                            </div>↵                    <div class="t4"><span>沙滩 岛屿</span></div>↵                </dd>↵            </dl>↵            <div class="desc"><strong>残</strong>三丘田码头是24小时都有轮船往返，不管你玩到何时，往返都不必担心的。↵轮船靠岸了，我随着兴奋的游客们...</div>        </a>↵            <a href="/poi/823.html?fromMdd=10132" class="poi">↵            <dl>↵                <dt><img src="https://b2-q.mafengwo.net/s8/M00/D7/5E/wKgBpVVmvq-AP0i9AAY0N-VZb-492.jpeg?imageMogr2%2Fthumbnail%2F%21250x170r%2Fgravity%2FCenter%2Fcrop%2F%21250x170%2Fquality%2F100" width="100%" alt=""/></dt>↵                <dd>↵                    <p class="t1" title="厦门大学">厦门大学↵                        <span class="tag">推荐</span>                        ↵                    </p>↵                    <p class="t2"></p>↵                    <div class="t3">↵                                                    <strong class="num">10745</strong>条蜂评 ，                            <strong class="num">3342</strong>篇游记提到                                            </div>↵                    <div class="t4"><span>学校</span></div>↵                </dd>↵            </dl>↵            <div class="desc"><strong>KOBEaholic</strong>厦大的开放是有时间限制的，中午的话12点到14点才可以进而且限制人数，晚上的话17点到21点可以进但是不...</div>        </a>↵            <a href="/poi/93149.html?fromMdd=10132" class="poi">↵            <dl>↵                <dt><img src="https://n3-q.mafengwo.net/s8/M00/F4/90/wKgBpVVBoeSACUbnAA0psFkAotw33.jpeg?imageMogr2%2Fthumbnail%2F%21250x170r%2Fgravity%2FCenter%2Fcrop%2F%21250x170%2Fquality%2F100" width="100%" alt=""/></dt>↵                <dd>↵                    <p class="t1" title="中山路步行街">中山路步行街↵                                                ↵                    </p>↵                    <p class="t2"></p>↵                    <div class="t3">↵                                                    <strong class="num">6971</strong>条蜂评 ，                            <strong class="num">1484</strong>篇游记提到                                            </div>↵                    <div class="t4"><span>特色街道/街区</span></div>↵                </dd>↵            </dl>↵            <div class="desc"><strong>二姑娘</strong>人山人海的中山路步行街，建筑的确是很有风情，小店也的确是文艺色彩浓厚，理想的摆拍好去处，小吃嘛，...</div>        </a>↵            <a href="/poi/22240.html?fromMdd=10132" class="poi">↵            <dl>↵                <dt><img src="https://b1-q.mafengwo.net/s10/M00/38/89/wKgBZ1lGgbqABkyPAA5tTcLM0Yg62.jpeg?imageMogr2%2Fthumbnail%2F%21250x170r%2Fgravity%2FCenter%2Fcrop%2F%21250x170%2Fquality%2F100" width="100%" alt=""/></dt>↵                <dd>↵                    <p class="t1" title="曾厝垵">曾厝垵↵                        <span class="tag">推荐</span>                        ↵                    </p>↵                    <p class="t2"></p>↵                    <div class="t3">↵                                                    <strong class="num">6455</strong>条蜂评 ，                            <strong class="num">1882</strong>篇游记提到                                            </div>↵                    <div class="t4"><span>特色街道/街区</span></div>↵                </dd>↵            </dl>↵            <div class="desc"><strong>KOBEaholic</strong>曾厝垵其实它跟什么磁器口锦里田子坊真的差不多，无非就是一个逛吃逛吃的地方。我觉得不一样的地方在于...</div>        </a>↵            <a href="/poi/843.html?fromMdd=10132" class="poi">↵            <dl>↵                <dt><img src="https://p1-q.mafengwo.net/s11/M00/AB/F3/wKgBEFrIXD2ARFYOAAWA4baJZHw07.jpeg?imageMogr2%2Fthumbnail%2F%21250x170r%2Fgravity%2FCenter%2Fcrop%2F%21250x170%2Fquality%2F100" width="100%" alt=""/></dt>↵                <dd>↵                    <p class="t1" title="南普陀寺">南普陀寺↵                        <span class="tag">推荐</span>                        ↵                    </p>↵                    <p class="t2"></p>↵                    <div class="t3">↵                                                    <strong class="num">6281</strong>条蜂评 ，                            <strong class="num">2024</strong>篇游记提到                                            </div>↵                    <div class="t4"><span>寺庙</span></div>↵                </dd>↵            </dl>↵            <div class="desc"><strong>大脸葱花</strong>五年前来过。门口没什么变化。但是旅游团很多很多啊！！超级多。↵南普陀对面就是厦门大学。寺庙前面是一...</div>        </a>↵        </section>↵                        <div id="btn_getmore" style="position: relative;text-align: center;padding: 20px;">↵                <a style="border: none;color:#ffdb26;font-size:16px;">↵                    <img src="https://c4-q.mafengwo.net/s10/M00/16/D2/wKgBZ1o3WXOAZQ-vAAAHM2Kece0574.png" width="15px;" style="margin-top: -3px;">↵                    &nbsp;&nbsp;加载更多↵                </a>↵            </div>↵
"""
u=re.findall("<a href=\"(.*?)\" class=\"poi\">",url)
l=re.findall("<p class=\"t1\" title=\"(.*?)\">",url)
print(u)
print("".join(l))
sp="热门：1.0"
print sp.split("：")[-1]