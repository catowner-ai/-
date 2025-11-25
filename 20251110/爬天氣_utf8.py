# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:19:12 2020

@author: user
"""

import csv
import urllib.request
from  bs4 import BeautifulSoup

url = "http://www.weather.com.cn/weather/101270101.shtml"
header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")  # 設置頭部信息
opener = urllib.request.build_opener()  # 修改頭部信息
opener.addheaders = [header]         #修改頭部信息
request = urllib.request.Request(url)   # 製作請求
response = urllib.request.urlopen(request)   #  得到請求的應答包



html = response.read()   #將應答包裏面的內容讀取出來
html = html.decode('utf-8')    # 使用utf-8進行編碼，不重新編碼就會成亂碼


final = []   #初始化一個空的list，我們爲將最終的的數據保存到list
bs = BeautifulSoup(html,"html.parser")   # 創建BeautifulSoup對象
body = bs.body  # 獲取body部分
data = body.find('div',{'id':'7d'})  # 找到id爲7d的div



ul = data.find('ul')  # 獲取ul部分
li = ul.find_all('li')  # 獲取所有的li
# print (li)
 
i = 0
for day in li:  # 對每個li標籤中的內容進行遍歷
    if i < 7:
        temp = []
        date = day.find('h1').string # 找到日期
#         print (date)
        temp.append(date)  # 添加到temp中
    #     print (temp)
        inf = day.find_all('p')  # 找到li中的所有p標籤
        # print(inf)
        # print (inf[1])
        temp.append(inf[0].string)  # 第一個p標籤中的內容（天氣狀況）加到temp中
        if inf[1].find('span') is None:
            temperature_highest = None # 天氣預報可能沒有當天的最高氣溫（到了傍晚，就是這樣），需要加個判斷語句,來輸出最低氣溫
        else:
            temperature_highest = inf[1].find('span').string # 找到最高溫度
            temperature_highest = temperature_highest.replace('℃', '') # 到了晚上網站會變，最高溫度後面也有個℃
        temperature_lowest = inf[1].find('i').string  #找到最低溫度
        temperature_lowest = temperature_lowest.replace('℃', '')  # # 最低溫度後面有個℃，去掉這個符號
        temp.append(temperature_highest)
        temp.append(temperature_lowest)
        final.append(temp)
        i = i +1
        
# print(final)

with open('weather.csv', 'a', errors='ignore', newline='',encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(final)