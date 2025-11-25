# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:24:35 2021

@author: OfficePC
"""

def calculator_value(Nowvalue,double,value=1):# 10 , True , 5
    if double == True:
        value=value*2
    Nowvalue = Nowvalue + value
    return Nowvalue


value=5
Nowvalue=10

New_value = calculator_value(Nowvalue,True,value)
print(New_value)


New2_value = calculator_value(Nowvalue,True)
print(New2_value)