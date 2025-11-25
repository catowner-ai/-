# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:58:34 2023

@author: USER
"""

#2023_4月版本

import requests
from bs4 import BeautifulSoup

title=[]
link_url=[]

r=requests.get('https://tw.yahoo.com/')

if r.status_code==requests.codes.ok:
    soup=BeautifulSoup(r.text,'html.parser')
    
    stories=soup.find_all('a',class_='Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)')
    for s in stories:
        print("標題:"+s.text)
        title.append(s.text)
        print("網址:"+s.get('href'))
        link_url.append(s.get('href'))

print(len(title))
print(link_url)



#%%

#2025_9月版本

import requests
from bs4 import BeautifulSoup

title=[]
link_url=[]

# # 有429的status_code  (所以無法正常進入解析資料的動作，也就是「不會進入」if裡的程式)
# r=requests.get('https://tw.yahoo.com/')


#正常版收到200 ok 的status code  (正常進入解析資料的動作，也就是  「進入」if裡的程式)
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
r=requests.get('https://tw.yahoo.com/',headers=headers)

print("status_code is = ",r.status_code)

if r.status_code==requests.codes.ok:
    print("ready to get message")
    
    soup=BeautifulSoup(r.text,'html.parser')
    
    stories=soup.find_all('a',class_='after:tw-stretched-box block')
    
    for s in stories:
        print("標題:"+s.text)
        title.append(s.text)
        print("網址:"+s.get('href'))
        link_url.append(s.get('href'))
else:
    print("no data")


print(len(title))
print(link_url)