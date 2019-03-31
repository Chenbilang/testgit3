#coding=utf-8
import time
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium
import json
from lxml import etree
class Test:
    def t(self):
            item = {}

            driver2 = webdriver.Chrome('C:\Google\Chrome\Application\chromedriver.exe')
            driver2.get('http://www.mafengwo.cn/jd/10208/gonglve.html')
            html = etree.HTML(driver2.page_source)
            spot_list = html.xpath("//div[@class='row row-allScenic']//div[@class='bd']/ul//li//a")
            for i in spot_list:
                item["spot"] = i.xpath("./h3/text()")[0]
                spot_url = i.xpath("./@href")[0]
                item["spot_url"] = "http://www.mafengwo.cn" + spot_url
                item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
                item_json = json.dumps(item, ensure_ascii=False, indent=2)
                print item_json
            # driver2.find_element_by_xpath("//a[@class='pi pg-next']").click()
            # WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'下一页')]"))).click()
            page = 0
            while page < 5:
               page = page + 1
               xinwei = WebDriverWait(driver2, 5).until(
                   expected_conditions.element_to_be_clickable((By.XPATH, "//a[@class='pi pg-next']")))

               xinwei.click()
               time.sleep(3)
               html = etree.HTML(driver2.page_source)
               spot_list = html.xpath("//div[@class='row row-allScenic']//div[@class='bd']/ul//li//a")
               for i in spot_list:
                   item["spot"] = i.xpath("./h3/text()")[0]
                   spot_url = i.xpath("./@href")[0]
                   item["spot_url"] = "http://www.mafengwo.cn" + spot_url
                   item["spot_id"] = re.findall("/(\d*)\.html", spot_url)[0]
                   item_json = json.dumps(item, ensure_ascii=False, indent=2)
                   print item_json






t=Test()
t.t()