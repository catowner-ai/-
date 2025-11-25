# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:57:23 2021

@author: OfficePC
"""

year = input("請輸入您出生的西元年份 : ")

print(type(year))

born = eval(year)-1911

print(type(born))

message = "你出生在民國" + str(born) + "年"
print(type(message))

print(message)