# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:39:06 2023

@author: USER
"""
#2023_4月版本

import requests
from bs4 import BeautifulSoup
title=[]
link_url=[]

r=requests.get('https://tw.news.yahoo.com/')

if r.status_code==requests.codes.ok:
    soup=BeautifulSoup(r.text,'html.parser')
    
    stories=soup.find_all('a',class_='D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)')
    for s in stories:
        print("標題:"+s.text)
        title.append(s.text)
        print("網址:"+s.get('href'))
        link_url.append(s.get('href'))

print(title)
print(link_url)



#%%    https://tw.news.yahoo.com/

#2025_9月版本

import requests
from bs4 import BeautifulSoup

yahoo_news_title=[]
yahoo_news_link_url=[]

# # 有429的status_code  (所以無法正常進入解析資料的動作，也就是「不會進入」if裡的程式)
# r=requests.get('https://tw.yahoo.com/')


#正常版收到200 ok 的status code  (正常進入解析資料的動作，也就是  「進入」if裡的程式)
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
r=requests.get('https://tw.news.yahoo.com/',headers=headers)

print("status_code is = ",r.status_code)

if r.status_code==requests.codes.ok:
    print("ready to get message")
    
    soup=BeautifulSoup(r.text,'html.parser')
    
    stories=soup.find_all('a',class_='D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)')
    
    for s in stories:
        print("標題:"+s.text)
        yahoo_news_title.append(s.text)
        print("網址:"+s.get('href'))
        yahoo_news_link_url.append(s.get('href'))
else:
    print("no data")


print(len(yahoo_news_title))
print(yahoo_news_link_url)



#%%  https://tw.sports.yahoo.com/



#2025_9月版本

import requests
from bs4 import BeautifulSoup

yahoo_sports_title=[]
yahoo_sports_link_url=[]

# # 有429的status_code  (所以無法正常進入解析資料的動作，也就是「不會進入」if裡的程式)
# r=requests.get('https://tw.yahoo.com/')


#正常版收到200 ok 的status code  (正常進入解析資料的動作，也就是  「進入」if裡的程式)
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
r=requests.get('https://tw.sports.yahoo.com//',headers=headers)

print("status_code is = ",r.status_code)

if r.status_code==requests.codes.ok:
    print("ready to get message")
    
    soup=BeautifulSoup(r.text,'html.parser')
    
    stories=soup.find_all('a',class_='Fw(b) Fz(18px) Lh(21px) LineClamp(2,42px) Fz(16px)!--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')
    
    for s in stories:
        print("標題:"+s.text)
        yahoo_sports_title.append(s.text)
        print("網址:"+s.get('href'))
        yahoo_sports_link_url.append(s.get('href'))
else:
    print("no data")


print(len(yahoo_sports_title))
print(yahoo_sports_link_url)
