# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re


# chrome driver 及 chrome options的設定

date_list=[]
title_list=[]
price_list=[]
url_list=[]
prices_list=[]
final_prices=[]


# ref : https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/
# ref : https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_chromium/selenium.webdriver.chromium.options.html
# ref : https://www.selenium.dev/documentation/webdriver/browsers/chrome/

options_obj=webdriver.ChromeOptions()



#www.etmall.com.tw要求下列權限  --> 設定成-->跳窗不顯示  
param={
       'profile.default_content_setting_values':
           {
               'notifications':1}
       }
    
options_obj.add_experimental_option('prefs',param)



#新版的設定方式，把chrome 目前受到自動測試軟體控制-->設定成不顯示
options_obj.add_experimental_option('excludeSwitches',['enable-automation'])  


#舊版的設定方式，把chrome 目前受到自動測試軟體控制-->設定成不顯示
# options.add_argument("disable-infobars") 

browser=webdriver.Chrome(options=options_obj) #建立瀏覽器物件


#%%

# 爬取資料

# browser=webdriver.Chrome() #建立瀏覽器物件

# browser.get("https://www.etmall.com.tw/Search?keyword=%E6%97%A5%E6%9C%AC") #開啟 Google

browser.get("https://www.etmall.com.tw/c3/78532") #改爬取日本旅遊的相關資訊

time.sleep(1)

# print(browser.page_source)


#%%


# 解析資料


soup = BeautifulSoup(browser.page_source,'html.parser')

date=soup.select(r'p.n-sale--subtitle')
print(date)
     

titles = soup.select(r'p.n-name a')
print(titles)

#re.compile('price_*')
prices = soup.find_all('span',class_='n-final-price')  #n-final-price
print(prices)


for i in prices:
    prices_list.append(i.text)
# print(prices_list)
# print(prices_list[1::2])  # $,12400,$,14700,

final_prices=prices_list
print(final_prices)
       

for datelist,title,price in zip(date,titles,final_prices):
    # print(datelist.text) 
    # print(title.text)
    # # print(title.get('href'))
    # print('https://www.etmall.com.tw'+title.get('href'))
    # print(price) 
      
#        # print(title.get('title'))
       
# #     # print(price.text)
 

#%%儲存資料

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