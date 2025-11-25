# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:04:28 2021

@author: OfficePC
"""
x=5
y=10

#list 列表 ，串列  --> 一個變數(容器)可以存多筆數據，中括號表示 []

lista = [1,2,3,99,99,99]
listb = [4,5,6,100,100,100]
listc = lista+listb  # [1,2,3,4,5,6]
listd = listc*2 # [1,2,3,4,5,6] *2  --> [1,2,3,4,5,6,1,2,3,4,5,6]
print(listd)