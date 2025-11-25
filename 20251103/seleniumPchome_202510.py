# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

#%% 202409版

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

# 20251103新版本，能抓到資料
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


#觀察網頁看到的<div class="c-prodInfoV2__title" title="Apple 蘋果 iPhone 17 Pro (512G)" data-regression="store_prodName">Apple 蘋果 iPhone 17 Pro (512G)</div>
#多筆資料
titles = soup.select('div.c-prodInfoV2__title')


#觀察網頁看到的<div class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m">$46,900</div>
#多筆資料
prices = soup.select('div.c-prodInfoV2__priceValue--m')






#網址抓取方式一
#觀察網頁看到的<div class="c-prodInfoV2 c-prodInfoV2--gridCard" data-soldout="false" tabindex="0"><a class="c-prodInfoV2__link gtmClickV2" href="/prod/DYAJ87-1900J84CN"><div class="c-prodInfoV2__flex"><div class="c-prodInfoV2__head"><div class="c-prodInfoV2__img"><img src="https://img.pchome.com.tw/cs/items/DYAJ871900J84CN/000001_1761211736.jpg?width=320" alt="Apple iPhone 17 Pro (256G)" data-regression="store_prodImg"></div></div><div class="c-prodInfoV2__body"><div class="c-prodInfoV2__infoBox c-prodInfoV2__infoBox--storeProdInfoCard"><div class="c-prodInfoV2__prodTypeLabel"><ul class="c-prodInfoV2__prodTypeLabelBar"><li class="c-prodInfoV2__labelItem"><div class="c-label c-label--md"><div class="c-label__rectangle c-label__rectangle--primary"><i class="o-icons o-icons--arrival24h"></i></div></div></li></ul></div><div class="c-prodInfoV2__infoBox c-prodInfoV2__infoBox--alignmentTitle"><div class="c-prodInfoV2__text c-prodInfoV2__text--xs500Tertiary300">熱銷現貨 再送高透空壓殼+鋼化玻璃貼+鏡頭貼</div><div class="c-prodInfoV2__title" title="Apple 蘋果 iPhone 17 Pro (256G)" data-regression="store_prodName">Apple 蘋果 iPhone 17 Pro (256G)</div></div><div class="c-prodInfoV2__priceBar"><div class="c-prodInfoV2__price" data-regression="store_prodPrice"><div class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m">$39,900</div></div></div><div class="c-prodInfoV2__salePrice"><div class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--xs">$39,900</div></div></div><div class="c-prodInfoV2__prodTypeLabel c-prodInfoV2__prodTypeLabel--activityLabelButtonSection"><ul class="c-prodInfoV2__prodTypeLabelBar"><li class="c-prodInfoV2__labelItem"><div class="c-label c-label--md"><div class="c-label__rectangle c-label__rectangle--grayLightest">P幣</div></div></li></ul></div></div></div></a><div class="c-prodInfoV2__otherFunctions"><ul class="c-prodInfoV2__list c-prodInfoV2__list--borderProdCardButtonGroup"><li class="c-prodInfoV2__item"><button class="btn btn--smAuto gtmClickV2" type="button" data-regression="store_addToWish" tabindex="0"><span class="btn__noFrame btn__noFrame--grayLighter"><i class="o-iconFonts o-iconFonts--actionHeartLine" data-regression="store_addToWish"></i></span></button></li><li class="c-prodInfoV2__item"><button class="btn btn--smAuto gtmClickV2" id="" type="button" data-regression="store_addToCart" tabindex="0"><span class="btn__noFrame btn__noFrame--grayLighter"><i class="o-iconFonts o-iconFonts--actionCart" data-regression="store_addToCart"></i></span></button></li></ul></div></div>
#網址用select方式抓取語法

#觀察網頁看到的<a class="c-prodInfoV2__link gtmClickV2" href="/prod/DYAJ87-1900J84CN"><div class="c-prodInfoV2__flex"><div class="c-prodInfoV2__head"><div class="c-prodInfoV2__img"><img src="https://img.pchome.com.tw/cs/items/DYAJ871900J84CN/000001_1761211736.jpg?width=320" alt="Apple iPhone 17 Pro (256G)" data-regression="store_prodImg"></div></div><div class="c-prodInfoV2__body"><div class="c-prodInfoV2__infoBox c-prodInfoV2__infoBox--storeProdInfoCard"><div class="c-prodInfoV2__prodTypeLabel"><ul class="c-prodInfoV2__prodTypeLabelBar"><li class="c-prodInfoV2__labelItem"><div class="c-label c-label--md"><div class="c-label__rectangle c-label__rectangle--primary"><i class="o-icons o-icons--arrival24h"></i></div></div></li></ul></div><div class="c-prodInfoV2__infoBox c-prodInfoV2__infoBox--alignmentTitle"><div class="c-prodInfoV2__text c-prodInfoV2__text--xs500Tertiary300">熱銷現貨 再送高透空壓殼+鋼化玻璃貼+鏡頭貼</div><div class="c-prodInfoV2__title" title="Apple 蘋果 iPhone 17 Pro (256G)" data-regression="store_prodName">Apple 蘋果 iPhone 17 Pro (256G)</div></div><div class="c-prodInfoV2__priceBar"><div class="c-prodInfoV2__price" data-regression="store_prodPrice"><div class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m">$39,900</div></div></div><div class="c-prodInfoV2__salePrice"><div class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--xs">$39,900</div></div></div><div class="c-prodInfoV2__prodTypeLabel c-prodInfoV2__prodTypeLabel--activityLabelButtonSection"><ul class="c-prodInfoV2__prodTypeLabelBar"><li class="c-prodInfoV2__labelItem"><div class="c-label c-label--md"><div class="c-label__rectangle c-label__rectangle--grayLightest">P幣</div></div></li></ul></div></div></div></a>

urls = soup.select('div.c-prodInfoV2--gridCard a')  # class="c-prodInfoV2 c-prodInfoV2--gridCard"  a --> 抓a tag

for url in urls :
    # print(url.get('href'))
    
    #https://24h.pchome.com.tw/+url  #完整的網址結合
    url_list.append('https://24h.pchome.com.tw'+url.get('href'))

print(url_list)



# #網址抓取方式二
# # 網址用find_all方式抓取語法
# urls=soup.find_all('a',class_='c-prodInfoV2__link gtmClickV2')

# for url in urls :
#     # print(url.get('href'))    
#     #https://24h.pchome.com.tw/+url  #完整的網址結合

#     url_list.append('https://24h.pchome.com.tw'+url.get('href'))

# print(url_list)





# prices = soup.find_all('span',id=re.compile('price_*'))
for title,price,url in zip(titles[2:],prices[2:],urls[2:]):
    # print(title.text)
    # # print('https:'+title.get('href'))
    # print(price.text[1:].replace(",",""))
    # print(url.get('href'))
    
    title_list.append(title.text)
    
                     # price.text -->$46,900　-->price.text[1:]  -->46,900
    price_list.append(price.text[1:].replace(",",""))
    url_list.append("https://24h.pchome.com.tw/"+url.get('href'))
    
print(title_list)
print(price_list)
print(url_list)

browser.quit()





# #%% 20251027版



# from selenium import webdriver #載入 webdriver 模組
# from bs4 import BeautifulSoup
# import time
# import re

# title_list=[]
# price_list=[]
# url_list=[]

# browser=webdriver.Chrome() #建立瀏覽器物件
# browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone17") #開啟 Google

# time.sleep(1)
# # print(browser.page_source)
# soup = BeautifulSoup(browser.page_source,'html.parser')

# titles = soup.select('div.c-prodInfoV2__title')
# for title in titles:
#     # print(title.text)
#     title_list.append(title.text)

# prices = soup.select('div.c-prodInfoV2__priceValue--m')  # class="c-prodInfoV2__priceValue c-prodInfoV2__priceValue--m"
# for price in prices:
#     # print(price.text)
#     price_list.append(price.text[1:])
    


# print(title_list)

# print("************")
 
# print(price_list)   


# # for title,price in zip(titles,prices):
# #     print(title.text)
# # #    print('https:'+title.get('href'))
# #     print(price.text)





# #%%
# urls = soup.select('div.c-prodInfoV2--gridCard a')  # class="c-prodInfoV2 c-prodInfoV2--gridCard"  a --> 抓a tag
# for url in urls :
#     # print(url.get('href'))
    
#     #https://24h.pchome.com.tw/+url  #完整的網址結合
#     url_list.append('https://24h.pchome.com.tw'+url.get('href'))

# print(url_list)


# # prices = soup.find_all('span',id=re.compile('price_*'))
# # for title,price in zip(titles,prices):
# #     print(title.text)
# #     print('https:'+title.get('href'))
# #     print(price.text)
    


# # prices = soup.find_all('span',id=re.compile('price_*'))
# # for title,price in zip(titles,prices):
# #     print(title.text)
# #     print('https:'+title.get('href'))
# #     print(price.text)
    
# browser.quit()








