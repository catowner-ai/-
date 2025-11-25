# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 21:22:29 2025

@author: USER
"""

#%%
import requests
from bs4 import BeautifulSoup
import requests

google_iphone17_title=[]
google_iphone17_link_url=[]


headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
# q=convid-19

# yahoo search
my_params = {'p': 'iphone17'}
r = requests.get('https://tw.search.yahoo.com/search',headers=headers,params=my_params)


#pchome
# r = requests.get('https://www.pchome.com.tw',headers=headers)  # r就是Response


# # google search
# my_params = {'q': 'iphone17'}
# r=requests.get('https://www.google.com.tw/search',headers=headers,params=my_params)

print(r.url)
print(r.status_code)



#%%
if r.status_code == requests.codes.ok:
    # print("DATA OK")
    # ##以下是可能會不正確顯示資料，因未指定編碼
    # # print(r.text)   #直接印出資料，未轉換編碼  -->　pchome此時編碼是ISO-8859-1
    
    
    # #以下是正確顯示資料的方式
    # print(r.encoding)  #查詢當下回傳的Response的編碼
    # r.encoding = 'utf-8'  #轉換編碼格式符合程式環境
    # print(r.text)   #轉編碼格式後就可正常讀取
    soup=BeautifulSoup(r.text,'html.parser')
    
   # print(soup.prettify())
    
    google_iphone17=soup.find_all('a',class_='va-bot bcan1cb')
    
    for s in google_iphone17:
        print("標題:"+s.text)
        google_iphone17_title.append(s.text)
        print("網址:"+s.get('href'))
        google_iphone17.append(s.get('href'))
else:
    print("no data")