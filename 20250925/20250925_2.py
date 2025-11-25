# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:38:50 2024

@author: USER
"""
#%%

x1='A'

print(type(x1))


x2="apple" #(1) a (2)p (3)p  (4)l (5)e


#%%


print('\"Python\"程式設計')

print("\"Python程式設計\"\t程式設計")


print('\101')

print('\x41')

print('\u0041')

print ('\N{BLACK SPADE SUIT}')  

#https://zh.wikipedia.org/zh-tw/Unicode%E5%AD%97%E7%AC%A6%E5%88%97%E8%A1%A8

#%%

print(ord("A"))

print(ord('€'))

print(ord("a"))


print(ord("♠"))


#%%


print(chr(9824))

print(chr(65))

print(chr(8364))


#%%

print(len("python 程式設計"))

print(min("Python程式設計"))

print(max("Python程式設計"))

print(str(11.2))#把數值轉字串的動作

#%%

x=str(11.2)  #把數值轉字串的動作

print(type(x))


print(min("程式設計"))

print(ord("程"))
print(ord("式"))
print(ord("設"))
print(ord("計"))

print(max("程式設計"))

#%%

print("happy "+"new "+"year "+"to "+"louis")

print("happy"*3)

print('我' > 'A')

print('12' > 'A')

print('XYZ' == 'xyz')

print('lccnet' in 'abcdelccnetapple')

print('lccnet' not in 'abcdelccnetapple')

#%%

print('65'=='A')

s="Python程式設計"

print(s[5])

print(s[2:5])

print(s[3:7])

print(s[6:-1])

#%%

s1="Python程式設計"

print(s1[:2])

print(s1[2:])

#%%

s1="Python程式設計"

print(s1[-2:])

#%%

x="Hello"

X1=x.upper()
print(X1)

print(x.upper())
print(x)
#%%

print(x.lower())
print(x)

X2=x.lower()
print(X2)

#%%

print(x.swapcase())
print(x)

y="an apple a day"
print(y.title())

print(y)
y_title=y.title()
print(y_title)


print(x.replace('Hello','ABC'))
print(x)


y="apple is good"
print(str.capitalize('an egg'))
print(str.capitalize(y))
print(y)


y="apple is good"
print(str.title('an egg'))
print(str.title(y))
print(y)


#%%

print(str.isupper("Happy"))

print(str.isupper("HAPPY"))


print(str.islower("Happy"))

print(str.islower("happy"))

print(str.isidentifier("Happy"))

print(str.isidentifier("5happy"))

#%%

print(str.isspace('    '))

print(str.istitle('Happy New Year'))

#%%

x='eeeWotte Wow axWowaz Wow Wow tetWow'
print(x.count('Wow'))

print(x.startswith('Wow'))

print(x.endswith('Wow'))

print(x.find('Wow'))

print(x.rfind('Wow'))

#%%

print('      lccnet is good      '.strip())

x='      lccnet is good      '.strip()
print(len(x))

print('www.example.com'.strip('cmowz.'))

print('www.lccnet.com.tw'.strip('cmowz.'))

#%%

print('      lccnet is good      '.lstrip())

x='      lccnet is good      '.lstrip()
print(len(x))

print('www.example.com'.lstrip('cmowz.'))

print('www.lccnet.com.tw'.lstrip('cmowz.'))

#%%

print('      lccnet is good      '.rstrip())

x='      lccnet is good      '.rstrip()
print(len(x))

print('www.example.com'.rstrip('cmowz.'))

print('www.lccnet.com.tw'.rstrip('cmowz.'))


#%%

print("lccnet is good".center(20))

print("www.lccnet.com.tw lccnet is good ......".center(20))


print("lccnet is good".ljust(20))

print("www.lccnet.com.tw lccnet is good ......".ljust(20))

print("lccnet is good".rjust(20))

print("www.lccnet.com.tw lccnet is good ......".rjust(20))

#%%

print('-42'.zfill(8))

print('32'.zfill(7))

#%%

x="www.lccnet.com.tw"

print(format(x,'20'))
print(format(x,'>20'))
print(format(x,'<20'))
print(format(x,'^20'))


print(format("Hello,lccnet",'20'))


print(format("Hello,lccnet",'>20'))


print(format("Hello,lccnet",'^20'))


print(format("Hello,lccnet",'<20'))

#%%




x="www.lccnet.com.tw"
y="www.lccnet.com.tw"


print(format(x,'20'))
print(format(x,'>20'))
print(format(x,'<20'))
print(format(x,'^20'))


#%%
print(dir())


#%%

import math

print(dir())

x=math.pi

print(x)

print(math.sqrt(9))

#%%

import random

print(dir())

print(random.random())

print(random.randint(5, 10))

#%%

import random

fruits=['Apple','Banana','Tomoto','kiwi','orange'] #0,1,2,3,4
for i in range(8):  #0,1,2
    print(fruits[random.randint(0,len(fruits)-1)])
    
    
#%%
import statistics


lista=[1,2,3,4,5]

print(statistics.mean(lista))


#%%

import statistics as st

listb=[1,2,3,4,5]

# print(statistics.mean(lista))

print(st.mean(listb))

print(st.median(listb))




#import statistics as st

#可寫成meannumber = st.mean(example_list)

#from statistics import mean

# meannumber = mean(example_list)

#%%

from statistics import mean, median

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



