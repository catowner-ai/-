# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re

browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone") #開啟 Google

time.sleep(1)
# print(browser.page_source)
soup = BeautifulSoup(browser.page_source,'html.parser')

titles = soup.select('h5.prod_name a')
prices = soup.find_all('span',id=re.compile('price_*'))
for title,price in zip(titles,prices):
    print(title.text)
    print('https:'+title.get('href'))
    print(price.text)
    










browser.quit()