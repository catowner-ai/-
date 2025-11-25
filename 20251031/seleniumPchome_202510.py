# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

#%% 20251103版

# 舊版本，已不能抓到資料
from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re

browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone17") #開啟 Google

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





#%%

# 新版本，能抓到資料
from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re

title_list=[]
price_list=[]
url_list=[]

browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone17") #開啟 Google

time.sleep(1)
# print(browser.page_source)
soup = BeautifulSoup(browser.page_source,'html.parser')

titles = soup.select('div.c-prodInfoV2__title')

prices = soup.select('div.c-prodInfoV2__priceValue--m')



#網址用select方式抓取語法
urls = soup.select('div.c-prodInfoV2--gridCard a')  # class="c-prodInfoV2 c-prodInfoV2--gridCard"  a --> 抓a tag
for url in urls :
    # print(url.get('href'))
    
    #https://24h.pchome.com.tw/+url  #完整的網址結合
    url_list.append('https://24h.pchome.com.tw'+url.get('href'))

print(url_list)




# # 網址用find_all方式抓取語法
# urls=soup.find_all('a',class_='c-prodInfoV2__link gtmClickV2')
# for url in urls :
#     # print(url.get('href'))
    
#     #https://24h.pchome.com.tw/+url  #完整的網址結合
#     url_list.append('https://24h.pchome.com.tw'+url.get('href'))

# print(url_list)





# # prices = soup.find_all('span',id=re.compile('price_*'))
# for title,price,url in zip(titles[2:],prices[2:],urls[2:]):
#     # print(title.text)
#     # # print('https:'+title.get('href'))
#     # print(price.text[1:].replace(",",""))
#     # print(url.get('href'))
    
#     title_list.append(title.text)
#     price_list.append(price.text[1:].replace(",",""))
#     url_list.append("https://24h.pchome.com.tw/"+url.get('href'))
    
# print(title_list)
# print(price_list)
# print(url_list)

browser.quit()





#%% 20251027版



from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time
import re

title_list=[]
price_list=[]
url_list=[]

browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone17") #開啟 Google

time.sleep(1)
# print(browser.page_source)
soup = BeautifulSoup(browser.page_source,'html.parser')

titles = soup.select('div.c-prodInfoV2__title')
for title in titles:
    # print(title.text)
    title_list.append(title.text)

prices = soup.select('div.c-prodInfoV2__priceValue--m')  # class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m"
for price in prices:
    # print(price.text)
    price_list.append(price.text[1:])
    


print(title_list)

print("************")
 
print(price_list)   


# for title,price in zip(titles,prices):
#     print(title.text)
# #    print('https:'+title.get('href'))
#     print(price.text)





#%%
urls = soup.select('div.c-prodInfoV2--gridCard a')  # class="c-prodInfoV2 c-prodInfoV2--gridCard"  a --> 抓a tag
for url in urls :
    # print(url.get('href'))
    
    #https://24h.pchome.com.tw/+url  #完整的網址結合
    url_list.append('https://24h.pchome.com.tw'+url.get('href'))

print(url_list)


# prices = soup.find_all('span',id=re.compile('price_*'))
# for title,price in zip(titles,prices):
#     print(title.text)
#     print('https:'+title.get('href'))
#     print(price.text)
    


# prices = soup.find_all('span',id=re.compile('price_*'))
# for title,price in zip(titles,prices):
#     print(title.text)
#     print('https:'+title.get('href'))
#     print(price.text)
    
browser.quit()








