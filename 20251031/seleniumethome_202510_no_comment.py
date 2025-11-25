# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import re



date_list=[]
title_list=[]
price_list=[]
url_list=[]
prices_list=[]
final_prices=[]



options_obj=webdriver.ChromeOptions()




param={
       'profile.default_content_setting_values':
           {
               'notifications':1}
       }
    
options_obj.add_experimental_option('prefs',param)



options_obj.add_experimental_option('excludeSwitches',['enable-automation'])  

-infobars") 

browser=webdriver.Chrome(options=options_obj) 


#%%



browser.get("https://www.etmall.com.tw/c3/78532") 

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

 


    date_list.append(datelist.text)
    title_list.append(title.text)
    url_list.append('https://www.etmall.com.tw'+title.get('href'))
    price_list.append(price)
    
    
    
print(date_list)
print(title_list)
print(url_list)
print(price_list)
    

browser.quit()