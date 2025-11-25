# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:27:24 2023

@author: USER
"""


#Get request  (x)
from urllib import request

resp = request.urlopen('http://tw.yahoo.com')
print(resp.read().decode())



#%%
#Get request ok 
from urllib import request

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

#需要使用 url 和 headers 生成一個 Request 物件，然後將其傳入 urlopen 方法中
req = request.Request('http://tw.yahoo.com', headers=headers)


resp = request.urlopen(req)
print(resp.read().decode())


#%%

# ssl error
import urllib.request

with urllib.request.urlopen('https://www.ntut.edu.tw') as response:
    
      
   # html = response.read()
   html_data = response.read().decode()

# print(html)
print("*****************")
print(html_data)
    
  
    
#%% # 解決方法一 
import urllib.request
   
import ssl
# 
# SSL（Secure Sockets Layer）安全通訊端層，TLS（Transport Layer Security）傳輸層安全協定。

# 安全協議，用於在用戶的網頁瀏覽器和網路伺服器之間安全地交換資訊。
# 主要功能：

# SSL/TLS協定提供三種基本的安全服務：

# 保密：:加密所有傳輸的資料來保護資訊的機密性。

# 鑑別：:伺服器透過數位憑證向使用者證明其身份，可選的客戶端認證則反之。

# 完整性：:確保在傳輸過程中，資料沒有被竄改或破壞。
 
# This restores the same behavior as before.
ssl_data= ssl._create_unverified_context()


with urllib.request.urlopen('https://www.ntut.edu.tw', context=ssl_data) as response:
    
    
   # html = response.read()
   html_data = response.read().decode()

# print(html)
print("*****************")
print(html_data)





#%%
import urllib.request

import ssl
context = ssl._create_unverified_context()

f = urllib.request.urlopen('https://www.ntut.edu.tw', context=context)
f.read(2000).decode('utf-8')  #前2000個字


#%%

# import urllib.request
# import urllib.parse

# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# url = "https://www.ntut.edu.tw" % params
# with urllib.request.urlopen(url) as f:
#     f.read().decode('utf-8')



#%%
#Post request (x)
from urllib import request
resp = request.urlopen('http://www.yahoo.com',data=b'word=hello',timeout=0.01)
print(resp.read().decode())


#%%
#Post request ok 

from urllib import request
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


#需要使用 url 和 headers 生成一個 Request 物件，然後將其傳入 urlopen 方法中
req = request.Request('http://tw.yahoo.com', headers=headers)
resp = request.urlopen(req,timeout=1,data=b'p=iphone17')

# resp = request.urlopen(req,data=b'word=hello',timeout=0.01)
print(resp.read().decode())



#%%

from urllib import request
url = 'http://httpbin.org/get'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


#需要使用 url 和 headers 生成一個 Request 物件，然後將其傳入 urlopen 方法中
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read().decode())

#%%

from http import cookiejar
from urllib import request
url = 'https://www.yahoo.com'

#創建一個 cookiejar 對象
cookie = cookiejar.CookieJar()

#使用 HTTPCookieProcessor 創建 cookie 處理器
cookies = request.HTTPCookieProcessor(cookie)\

#並以它為參數創建 Opener 對象
opener = request.build_opener(cookies)

#yahoo需加入headers 方可存取
headers = ('user-agent', 'Mozilla/5.0' )
opener.addheaders=[headers]



#使用這個 opener 來發起請求
resp = opener.open(url)

#查看之前的 cookie 物件，則可以看到存取 yahoo 獲得的 cookie
for i in cookie:
    print("cookie value = ")
    print(i)
    
#%%

# ref : https://zh.wikipedia.org/zh-tw/%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8

from urllib import request
url = 'http://www.ntut.edu.tw'
proxy = {'http':'20.239.26.126:80','https':'20.239.26.126:80'}

#創建代理處理器
proxies = request.ProxyHandler(proxy)

#創建 opener 對象
opener = request.build_opener(proxies)
resp = opener.open(url)
print(resp.read().decode())

#%%

from urllib import request
url='http://python.org/'
request.urlretrieve(url,'lccnet.html')




