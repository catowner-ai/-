# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:55:56 2024

@author: Louis_office
"""

from sklearn import datasets
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns;sns.set()

rng=np.random.RandomState(8)  # 有設定亂數種子，每次產生的亂數都一樣

# rng=np.random  # 每次產生的亂數都不一樣

temp_data=rng.rand(50)  # 產生50筆亂數


#%%

x=10*rng.rand(50)
print(x)

z=rng.rand(50)
print(z)

x1=3*x
print(x1)

# y=ax   +b
y=3*x-5+rng.randn(50)

y1=3*x-5

print(y)
plt.scatter(x,y);
plt.scatter(x,y1);



#%%

rng=np.random.RandomState(2)

x2=10*rng.rand(50)

print(x2)

# # y=ax+b (a--> slop 斜率 )
y2=20*x-5+rng.randn(50)

print(y2)

plt.scatter(x,y2)


#%%

npq=np.random.rand(50)

#random 不固定
x=10*np.random.rand(50)

print(x)

y=10*x-5+np.random.randn(50)

print(y)

plt.scatter(x,y)


