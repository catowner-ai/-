# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:41:15 2023

@author: USER
"""
# ref : https://docs.python.org/zh-tw/3/library/re.html
# ref : https://regex101.com/
import re
string = '台中市南屯區埔興段35-1253號'
regex = re.compile(r'段(\d+-*\d*)')

# regex = re.compile(r'段(\d+-*\d*)(\d)(\d)')
match = regex.search(string)
print(match)


print(match.group(0))

print(match.group(1))

# print(match.group(2))

# print(match.group(3))

#%%

test_string='aabb abb aab dcd hab aee ab aaaaab aabbbbb'
pattern = 'a+b{2,4}'
ans=re.findall(pattern,test_string)
print(ans)

print(type(ans))

print(len(ans))



#%%

import re


str1="a9b"
print(re.findall(r"a.b",str1))


str2="a888afasdfb"
print(re.findall(r"a[A-Z,a-z,0-9]+b",str2))
print(re.findall(r"a\w+b",str2))


str3="find:591. , dot., yes., skip:mpon"
pattern = '.{3}\.'
ans=re.findall(pattern,str3)
print(ans)


str4='lccnet i love iphone17 , i love cats , i love lccnet, samsung , sony wii'
pattern = 'i love lccnet|i love cats | i love iphone17'
ans=re.findall(pattern,str4)
print(ans)

#%%
import re


str2="a  rerer%%b456456b"

print(re.findall(r"a(.+?)b",str1))

str1="a123b456b"
# ?控制只匹配0或1個!
print(re.findall(r"a(.+)b",str1))
print(re.findall(r"a(.*)b",str1))


print(re.findall(r"a(.+?)b",str2))
print(re.findall(r"a(.+)b",str2))
print(re.findall(r"a(.*)b",str2))

#%%
str3="a23b\na34b" 
 # a23b
 # a34b

re.findall(r"a(\d+)b.+a(\d+)b",str3)

re.findall(r"a(\d+)b.+a(\d+)b",str3,re.S)

str4="a23b\na34b\na99999b"
# a23b
# a34b
# a99999b
re.findall(r"^a(\d+)b",str4)

re.findall(r"^a(\d+)b",str4,re.M)

#%%

import re
match = re.search('(?P<name>.*) (?P<phone>.*) (?P<address>.*)', 'John 123456 Taipei')
print(match.group('name'))
print(match.group('phone'))
print(match.group('address'))
print(match)

