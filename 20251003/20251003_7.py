# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:38:14 2022

@author: OfficePC
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=x*2


plt.plot(x,y,"ro")
plt.plot(x**2,y**2,"bo")
plt.plot(x**3,y**3,"go")

plt.text(1,1,"Y=X*2")

plt.text(20,35,"Y=(X*2)**2")

plt.text(20,200,"Y=(X*2)**3")

plt.show()