# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:02:40 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
titlelist=[]
ithome_url=[]
times_list=[]
r = requests.get('https://www.ithome.com.tw/',verify=False)


r.encoding = 'utf-8'
if r.status_code == 200:
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')

    # titles = soup.find_all('a')
    titles = soup.select('p.title a')
    #(a1,a2,a3,a4,a5,a6)
    #(1,2,3,4,5,6)
    
    times = soup.select('p.post-at')
    print('times data = ',times)
    
    for title,time in zip(titles,times):
        print(title.text.replace("\n",""))
        
        titlelist.append(title.text.replace("\n",""))
        # print('https://www.ithome.com.tw'+title.get('href'))
        ithome_url.append('https://www.ithome.com.tw'+title.get('href'))     
        times_list.append(time.text)
        
print(titlelist)
print("****************************")
print(ithome_url)
print("****************************")
print(times_list)


