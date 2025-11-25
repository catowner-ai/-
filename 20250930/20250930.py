# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:17:27 2024

@author: USER
"""

print(dir())

import math


print(dir())



#%%
print(math.pi)


print(math.sqrt(9))

import random

print(random.random())

print(random.randint(5, 10))

#%%

import random
fruits = ['Apple', 'Banana', 'Tomoto']
for i in range(3):
    print(fruits[random.randint(0, len(fruits)-1)])



import random

fruits=['Apple','Banana','Tomoto','kiwi','orange'] #0,1,2,3,4
for i in range(50):  #0,1,2
    print(fruits[random.randint(0,len(fruits)-1)])
    
    
#%%
import statistics


lista=[1,2,3,4,5,577,312,3254,3215,545]

print(statistics.mean(lista))


#%%

import statistics as st

listb=[1,2,3,4,5,6,8]

# print(statistics.mean(lista))

print(st.mean(listb))

print(st.median(listb))




#import statistics as st

#可寫成meannumber = st.mean(example_list)

#from statistics import mean

# meannumber = mean(example_list)

#%%

from statistics import mean, median
listc=[1,2,3,4,5]

# print(statistics.mean(lista))

print(mean(listc))

print(median(listc))

#%%

from statistics import mean as m, median as d


listc=[1,2,3,4,5]

# print(statistics.mean(lista))

print(m(listc))

print(d(listc))




#%%


from statistics import *

mean([1,2,3,4,5])





#%%

import statistics

listvalue = [10,15,23,8,57,47,26,10,15,28,23]

stdevnumber=statistics.stdev(listvalue)
print("標準差為 : ",stdevnumber)

variancenumber = statistics.variance(listvalue)
print('變異數為', variancenumber)

meannumber = statistics.mean(listvalue)
print('平均數為', meannumber)

mediannumber = statistics.median(listvalue)
print('中位數為', mediannumber)

#%%

import statistics as st

listvalue = [10,15,23,8,57,47,26,10,15,28,23]

stdevnumber=st.stdev(listvalue)
print("標準差為 : ",stdevnumber)

variancenumber = st.variance(listvalue)
print('變異數為', variancenumber)

meannumber = st.mean(listvalue)
print('平均數為', meannumber)

mediannumber = st.median(listvalue)
print('中位數為', mediannumber)


#%%

from statistics import *

listvalue = [10,15,23,8,57,47,26,10,15,28,23]

stdevnumber= stdev(listvalue)
print("標準差為 : ",stdevnumber)

variancenumber = variance(listvalue)
print('變異數為', variancenumber)

meannumber = mean(listvalue)
print('平均數為', meannumber)

mediannumber = median(listvalue)
print('中位數為', mediannumber)



#%%

import calendar
x=calendar.prmonth(2025, 10)
print(x)


y=calendar.prcal(2025) 
print(y)



#%%

import datetime
# x=datetime.timezone(datetime.timedelta(hours=0))
x=datetime.timezone(datetime.timedelta(hours=8))
print(x)



d1 = datetime.datetime(2025, 6, 24)
d2 = datetime.datetime(2025, 7, 28)
print((d1))
print((d2))

print(type(d1))
print(type(d2))

print((d2-d1))

print((d2-d1).days)

#%%

print(datetime.datetime.now())

print(datetime.datetime(2025,9,30).weekday())


#%%
import time
a=time.strftime("%Y-%m-%d %X",time.localtime())
print(a)

b=time.strftime("%y-%m-%d %A",time.localtime())
print(b)

#%%

import time
a = '2023/02/06 14:02:25'
print(type(a))

t = time.strptime(a,'%Y/%m/%d %H:%M:%S')
print(type(t))
print(t)




print(t.tm_year)
print(t.tm_min)
print(t.tm_sec)



w=time.strftime('%Y年-%m月-%d日',t) 
w2=time.strftime('%Y/%m/%d',t) 


print(w)
print(type(w))

print(w2)
print(type(w2))
#strftime()時間轉字串

#%%
# ssl error


import urllib.request
import ssl

# Create an SSL context that does not verify certificates
ssl_context = ssl._create_unverified_context()

# Use the SSL context with urllib
response = urllib.request.urlopen('http://www.ntu.edu.tw/', context=ssl_context)
print(response.read())



#%%
# import urllib.request; #用來建立請求

from urllib.request import urlopen


html = urlopen("http://www.ntu.edu.tw/")
print(html)


print(html.read())


#%%

from urllib.request import urlopen

html = urlopen("https://docs.python.org/3/tutorial/datastructures.html")

print(html)

print(html.read)

