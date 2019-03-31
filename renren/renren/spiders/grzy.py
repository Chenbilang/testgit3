# -*- coding: utf-8 -*-
import scrapy



class GrzySpider(scrapy.Spider):
    name = 'grzy'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/969552498/profile']

    def start_requests(self):
        cookies="anonymid=jrluzwevd5luuh; depovince=GUZ; jebecookies=ac849843-5659-41b8-a108-dd37ad422739|||||; _r01_=1; JSESSIONID=abcRVcLk8bvw64y-0BOIw; ick_login=839f2270-e8c2-48a4-9a07-b2923eed303a; _de=7F4DFC776882A6DD1D8A9C8904137FAA; p=67c1cb3f89b838bb392d1e0491e952cc8; first_login_flag=1; ln_uact=13533642854; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=825ddec9f2e4f947e32212cfe1285d598; societyguester=825ddec9f2e4f947e32212cfe1285d598; id=969552498; xnsid=57908598; ver=7.0; loginfrom=null; springskin=set; wp_fold=0"
        cookies={i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )
    def parse(self, response):
        print (response.body.decode("utf-8"))
