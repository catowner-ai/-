# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:53:14 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
# r=requests.Session()
# payload={
#     "from":"bbs/Gossiping/index.html",
#     "yes":"yes"}

# r1=r.post("https://www.ptt.cc/ask/over18",payload)
# r2=r.get("https://www.ptt.cc/bbs/Gossiping/index.html")
# print(r2.text)


url="https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(5):
    r1=requests.get(url)
    if r1.status_code==requests.codes.ok:
        soup=BeautifulSoup(r1.text,'html.parser')
        sel=soup.select("div.title a") #標題
        
        u=soup.select("div.btn-group.btn-group-paging a")
        url="https://www.ptt.cc"+u[1]["href"] #新網頁(網址)的新連結
        for s in sel:
            print(s["href"],s.text)
    else:
        print("get data error")