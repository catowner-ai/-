# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:21:00 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/joke/index.html"


for i in range(5):
    r=requests.get(url)
    if r.status_code==requests.codes.ok:
        soup=BeautifulSoup(r.text,'html.parser')
        sel=soup.select("div.title a") #標題
        
        u=soup.select("div.btn-group.btn-group-paging a")
        url="https://www.ptt.cc"+u[1]["href"] #新網頁(網址)的新連結
        for s in sel:
            print(s["href"],s.text)
    