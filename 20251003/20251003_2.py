# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:50:11 2022

@author: OfficePC
"""

import numpy as np
import matplotlib.pyplot as plt 


x=np.arange(0,5,0.1)
print(x)

# plt.plot(x,x,"r--",x,x**2,"bs",x,x**3,"g^")
# plt.show()

plt.plot(x,x,"r--")
# plt.show()

plt.plot(x,x**2,"bs")
# plt.show()


plt.plot(x,x**3,"g^")
# plt.show()

plt.plot(x,x**3,"y^")
