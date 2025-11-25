# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:57:28 2021

@author: OfficePC
"""

def get_discount(kid, senior):
    discount = 0.1
    if not (kid or senior):
        discount = 0
    return discount

discount_value=get_discount(False,False) # 0
print(discount_value)