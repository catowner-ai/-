# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:28:20 2023

@author: USER
"""
# ref : https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification



import requests
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
# r = requests.get('https://api.github.com/events')

# r = requests.get('https://api.github.com/user')
r = requests.get('https://www.ntust.edu.tw/',headers=headers,verify=False)

print(r.status_code)

if r.status_code == requests.codes.ok:
    print("get data OK")
    print(r.text)
    
 
#%%    
# r = requests.post('https://www.pchome.com.tw', data={'key': 'value'})


##舊版的寫法
# r = requests.post('https://www.pchome.com.tw', data={'key': 'value'})


#新版的寫法
# r = requests.get('https://www.pchome.com.tw', params={'key': 'value'})


#範例 : 爬取yahoo 輸入關鍵字  



# r = requests.get('https://www.yahoo.com.tw', params={'p': 'iphone17'})  # status code =429


# https://tw.search.yahoo.com/search?p=iphone17  #從網頁觀察到的

# r = requests.get('https://tw.search.yahoo.com/search', params={'p': 'iphone17'})  # status code =500

# r = requests.get('https://tw.yahoo.com/', params={'p': 'iphone17'})  # status code =500


#正確爬取方式1 直接固定網址
r = requests.get('https://tw.search.yahoo.com/search?p=iphone17',headers=headers)

#正確爬取方式1 參數的代入方式 
# r = requests.get('https://tw.search.yahoo.com/search', params={'p': 'iphone17'},headers=headers) 

print(r.status_code)

# 輸出網頁HTML 原始碼
if r.status_code == requests.codes.ok:
    print(r.url)
    print("OK")
    # print(r.text)

#%%

# 查詢參數
my_params = {'key1': 'value1', 'key2': 'value2'}


# 將查詢參數加入GET 請求中
r = requests.get('http://httpbin.org/get', params = my_params)

# # 將查詢參數直接用網址來加入get
# r = requests.get('http://httpbin.org/get?key1=value1&key2=value2')

print(r.url)




#%%

import requests

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
# q=convid-19

# yahoo search
my_params = {'p': 'iphone17'}
# r = requests.get('https://tw.search.yahoo.com/search',headers=headers,params=my_params)


#pchome
# r = requests.get('https://www.pchome.com.tw',headers=headers)  # r就是Response


# # google search
my_params = {'q': 'iphone17'}
r=requests.get('https://www.google.com.tw/search',headers=headers,params=my_params)

print(r.url)
print(r.status_code)


if r.status_code == requests.codes.ok:
    print("DATA OK")
    
    
    ##以下是可能會不正確顯示資料，因未指定編碼
    # print(r.text)   #直接印出資料，未轉換編碼  -->　pchome此時編碼是ISO-8859-1
    
    
    #以下是正確顯示資料的方式
    print(r.encoding)  #查詢當下回傳的Response的編碼
    # r.encoding = 'utf-8'  #轉換編碼格式符合程式環境
    # print(r.text)   #轉編碼格式後就可正常讀取

#%%

# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}
# 將資料加入POST 請求中

#新版的寫法
r = requests.post('http://httpbin.org/post', params= my_data)
print(r.url)

#%%

#%%

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
# q=convid-19
my_params = {'q': 'iphone17'}

r = requests.get('https://www.google.com.tw/search', params= my_params,headers=headers)
print(r.url)

if r.status_code == requests.codes.ok:
    print("OK")
    print(r.text)

#%%
import requests
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=payload)

print("status_code = ", r.status_code)

print(r.url)
print(r.text)


#%%
# 具有重複鍵值的資料

my_data = (('key1', 'value1'), ('key1', 'value2'))


# 將資料加入POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)

print("status_code = ", r.status_code)

print(r.url)
print(r.text)

#%%

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
##具有重複鍵值的資料
##帶參數送出request

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('https://tw.yahoo.com', params=payload)


#不帶參數送出request
r = requests.get('https://tw.yahoo.com',headers=headers)


print("url = ",r.url)
# print("text = ",r.text)
print("encoding = ",r.encoding)
print("___________________")
print(r.headers)
print(r.headers['date'])


# print(r.content)

#%%

import requests

r = requests.get('https://api.github.com/events')

# print(r.text)

print(r.json())



#%%

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)


payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)


print(r2.text)

#%%

my_files = {'my_filename': open('lccnet.txt', 'rb')}
# 將檔案加入POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)

print("url = ",r.url)
print("text = ",r.text)
print("encoding = ",r.encoding)
print("___________________")
print("headers = ",r.headers)
print("date = " , r.headers['date'])
print("Content-Length = ",r.headers['Content-Length'])

#%%
url = 'https://httpbin.org/cookies'

#方式一
cookie = dict(name='louis')

# #方式二
# cookie = {"name":'louis',"tel":"apple"}

r = requests.get(url, cookies=cookie)
print(r.text)

#%%

r = requests.get('http://github.com/')
print(r.url)
print(r.status_code)
print(r.history)

#%%

r = requests.get('http://github.com/', allow_redirects=False)

print(r.status_code)

print(r.history)

#%%

r = requests.get('http://github.com/', allow_redirects=True)

print(r.status_code)

print(r.history)


#%%


requests.get('https://tw.yahoo.com', timeout=0.01)

print("louis")


#%%
import requests
session = requests.Session()
print(type(session))

response = session.get('http://httpbin.org/cookies',cookies={'from-my':'browser'})
print(response.text)













