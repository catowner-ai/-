# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:53:22 2025

@author: USER
"""
import random

print(random.randrange(11,21,1))#不會取到終止值的數據

print("**********")
print(random.randrange(11,20,1))

#%%

print(random.randint(11,20))  #會取到終止值的數據
print("**********")
print(random.randint(11,21))