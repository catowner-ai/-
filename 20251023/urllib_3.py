# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:25:11 2023

@author: USER
"""

# ref : https://urllib3.readthedocs.io/en/stable/

import urllib3
http=urllib3.PoolManager()
r=http.request('GET','http://httpbin.org/robots.txt')
print(r.status)

print(r.data)
#%%
import urllib3
http=urlib3.poolmanager()
r=http.request('get','http://httpin.org/robots.txt')
print(r.status)

#%%　
#set headers
headers={'X-Something':'value'}
resp=http.request('GET','http://httpbin.org/headers',headers=headers)


#%%
#set url param (get)

fields={'arg':'value'}
resp=http.request('GET','http://httpbin.org/get',fields=fields)

#%%
#set url param (post)

fields={'arg':'value'}
resp=http.request('POST','http://httpbin.org/post',fields=fields)

#%%
#Query parameters

r=http.request('GET','http://httpbin.org/get',fields={'arg':'value'})



#%%
import urllib3
from urllib.parse import urlencode
http=urllib3.PoolManager()

params={'wd':'日本東京','code':1,'height':'190','Weight':80}

encoded_args=urlencode(params)



url='http://httpbin.org/post?'+encoded_args

r=http.request('POST',url)

print(r.read())
# print(r.getcode())
print(r.getheaders())
print(r.geturl())




#%%






