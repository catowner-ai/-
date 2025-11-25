# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:34:01 2021

@author: OfficePC
"""

data ="abcdefghijklmnopqrstuvwxyz"
#編號  0123456789

a=data[3:15] 
print(a)

b=data[3:15:3] 
print(b)

c=data[15:3:-3]
print(c)

d=data[::-3] 
print(d)

#參考解答 
# (1) -->c
# (2) -->F
# (3) -->B
# (4) -->A