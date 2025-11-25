# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# ref : https://useragent.onlinealat.com/

import urllib

# targetUrl="https://www.google.com.tw/search?q=iphone17"

targetUrl="https://www.pchome.com.tw"

# ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'

##帶user-agent
headers_data={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}
response = urllib.request.Request(targetUrl,headers=headers_data)

# #不帶user-agent
# response = urllib.request.Request(targetUrl)

# # 未指定編碼格式
# html_doc = urllib.request.urlopen(response).read()

#指定編碼格式解碼decode()
html_doc = urllib.request.urlopen(response).read().decode('utf-8')

print(html_doc)

#%%

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser')

print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent.name)

print(soup.a)

print(soup.p)

# # # soup.p['class']


# # soup.a

print(soup.find_all('a'))
