# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 13:49:19 2025

@author: USER
"""

lamf = lambda: "lccnet is good!"
print(lamf())  # 輸出: lccnet is good!

#%%

x = lambda y : y + 10
print(x(101))   

#%%

x = lambda a, b : a * b
print(x(10, 10))

#%%
apple = lambda a, b, c : a + b * c
print(apple(5, 6, 12))

#%%匿名函式
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)  # lambda a : a * 2
mytripler = myfunc(3)  # lambda a : a * 3

print(mydoubler(11))
print(mytripler(11))

#%%匿名函式

numbers = list(range(10))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 輸出：[2, 4, 6, 8]


#%%

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
