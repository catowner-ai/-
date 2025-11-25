# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023

@author: USER
"""

from selenium import webdriver #載入 webdriver 模組
from bs4 import BeautifulSoup
import time




date_list=[]
title_list=[]
price_list=[]
url_list=[]
prices_list=[]



#%%
# chrome driver 及 chrome options的設定

# ref : https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/
# ref : https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_chromium/selenium.webdriver.chromium.options.html
# ref : https://www.selenium.dev/documentation/webdriver/browsers/chrome/


# ref : https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/
# ref : https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_chromium/selenium.webdriver.chromium.options.html
# ref : https://blog.csdn.net/qq_35999017/article/details/123922952


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
#https://www.etmall.com.tw/c3/78532   #日本旅遊
#https://www.etmall.com.tw/c3/121916  #韓國旅遊

time.sleep(1)

# print(browser.page_source)


#%%
# 解析資料

soup = BeautifulSoup(browser.page_source,'html.parser')


# #等同於抓到這樣的資料<p class="n-sale--subtitle">2026/1/13</p>  ，多筆資料
date=soup.select(r'p.n-sale--subtitle')
print(date)
     
# #等同於抓到這樣的資料<a href="/i/100006282192" title="清艙~高雄爆省大阪日本環球影城瑪利歐.好運滿滿勝尾寺.大阪廚房黑門市場.日式燒肉吃到飽四日-SJP04KKK29" class="" rel="noreferrer noopener" target="_blank">清艙~高雄爆省大阪日本環球影城瑪利歐.好運滿滿勝尾寺.大阪廚房黑門市場.日式燒肉吃到飽四日-SJP04KKK29</a>
# #多筆資料
titles = soup.select(r'p.n-name a')
print(titles)

#re.compile('price_*')

# #等同於抓到這樣的資料<span class="n-final-price">21,462</span>
# #多筆資料
prices = soup.find_all('span',class_='n-final-price')  #n-final-price
print(prices)



#抓取出所有爬到的金額，再把,號去掉 -->純數字
for i in prices:
    prices_list.append(i.text.replace(",",""))  #i.text 抓到的是-->21,462 -->把,號去掉-->text.replace(",","") -->21462
    

for datelist,title,price in zip(date,titles,prices_list):
    # print(datelist.text) 
    # print(title.text)
    # # print(title.get('href'))
    # print('https://www.etmall.com.tw'+title.get('href'))
    # print(price) 
    



    
## 儲存至List      
    date_list.append(datelist.text)
    title_list.append(title.text)
    url_list.append('https://www.etmall.com.tw'+title.get('href'))# /c2/100296
                    #https://www.etmall.com.tw/c2/100296
    price_list.append(price)
      
#        # print(title.get('title'))
       
# #     # print(price.text)
 



#%%儲存資料

# # 儲存至List   
#     date_list.append(datelist.text)
#     title_list.append(title.text)
#     url_list.append('https://www.etmall.com.tw'+title.get('href'))
#     price_list.append(price)
    
    
#%% 輸出所有list的結果

    
print(date_list)
print(title_list)
print(url_list)
print(price_list)

browser.quit()