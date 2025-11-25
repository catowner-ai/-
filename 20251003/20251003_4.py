# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:21:48 2022

@author: OfficePC
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus']=False #負號呈現正常的語法


x=np.array([1,2,3,4,5,6,7,8,9,10])
y=x*2

plt.plot(x,y,'ro')

plt.axis([-10,10,-50,50])
plt.grid()
plt.show()