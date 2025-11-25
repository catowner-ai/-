# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:51:21 2023

@author: USER
"""

#urllib.parse.quote
from urllib import parse

keyword='日本東京'

#quote --> 將特殊字元進行 url 編碼
print(parse.quote(keyword))


#unquote --> 將url 編碼轉回 特殊字元
parse.unquote('%E6%97%A5%E6%9C%AC%E6%9D%B1%E4%BA%AC')


#%%


#urlencode
from urllib import parse
params={'wd':'日本東京','code':1,'height':'190','Weight':80}
parse.urlencode(params)


#%%

# ref  : https://docs.python.org/zh-tw/3.13/library/urllib.error.html

#urllib.error

from urllib import request
from urllib.error import HTTPError,URLError

try:
    request.urlopen('http://tw.yahoo.com') # HTTPError
    # request.urlopen('https://www.pchome2222.com.tw') # URLError
    
except HTTPError as e:
    print("HTTPError")
    print("e.code = ",e.code)
    print("e.reason = ",e.reason)
    print("e.headers = ",e.headers)
    
    
except URLError as e2:
    print("URLError")
    print(e2.reason)
    
