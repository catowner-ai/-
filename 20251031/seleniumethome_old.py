# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re


date_list=[]
title_list=[]
price_list=[]
url_list=[]
prices_list=[]
final_prices=[]
browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("https://www.etmall.com.tw/Search?keyword=%E6%97%A5%E6%9C%AC") #開啟 Google


time.sleep(1)
# print(browser.page_source)
soup = BeautifulSoup(browser.page_source,'html.parser')

date=soup.select(r'p.n-sale--subtitle')
# print(date)
     

titles = soup.select(r'p.n-name a')
# print(titles)

#re.compile('price_*')
prices = soup.find_all('span',class_='n-price--16')
# print(prices)


for i in prices:
    prices_list.append(i.text)
# print(prices_list)
# print(prices_list[1::2])  # $,12400,$,14700,
final_prices=prices_list[1::2]
print(final_prices)
       

for datelist,title,price in zip(date,titles,final_prices):
    # print(datelist.text) 
    # print(title.text)
    # # print(title.get('href'))
    # print('https://www.etmall.com.tw'+title.get('href'))
    # print(price) 
      
#        # print(title.get('title'))
       
# #     # print(price.text)
 
# 儲存至List   
    date_list.append(datelist.text)
    title_list.append(title.text)
    url_list.append('https://www.etmall.com.tw'+title.get('href'))
    price_list.append(price)
    
print(date_list)
print(title_list)
print(url_list)
print(price_list)
    










browser.quit()