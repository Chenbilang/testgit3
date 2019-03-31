# coding=utf-8
# 使用cookies登陆
import requests
import io
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
          }
cookies="anonymid=jrc545r7phh2bt; depovince=GUZ; _r01_=1; JSESSIONID=abcOPGvgNdmN_9DQdAfIw; ick=7ab1aa2b-6ec3-4f87-a047-bd5640624e44; vip=1; jebecookies=8ea86e02-e401-42bd-b404-7d617b66b280|||||; ick_login=f8857c2e-7646-40f3-9167-e9ced11222e6; _de=7F4DFC776882A6DD1D8A9C8904137FAA; p=ea919c922f5e4fa7c90d8cb47c2d82e48; first_login_flag=1; ln_uact=13533642854; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=bd2469b94554fa2ff72209310b4395c28; societyguester=bd2469b94554fa2ff72209310b4395c28; id=969552498; xnsid=7a79648e; loginfrom=syshome"
cookies={i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
print (cookies)
#使用post发送请求将会让cookie也保存其中

r=requests.get("http://www.renren.com/969552498",headers=headers, cookies=cookies)
print(r.status_code)
with io.open("renren3.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode("utf-8"))