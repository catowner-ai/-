# search(substring, string)

import re

print(re.search('iphone', 'iphone17 vs iphone14 pro')) 

re_result=re.search ('iphone', 'iphone17 vs iphone14 pro')

print(re_result)
# <re.Match object; span=(0, 6), match='iphone'>

#%%

print(re_result.group())  #回傳找到的子字串
print(re_result.start())     #起始位置
print(re_result.end())    #結束位置
print(re_result.span())   #所有相關位置資料

print(re.search('iphone18', 'iphone17 vs iphone14 pro')) 
