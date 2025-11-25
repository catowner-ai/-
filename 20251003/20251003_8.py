# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:38:52 2022

@author: OfficePC
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=x*2



plt.plot(x,y,"ro",label="Y=X*2")
plt.plot(x*2,y*2,"bo",label="Y=X**")
plt.plot(x*3,y*3,"yo",label="Y=3x")


plt.legend()
plt.legend(loc= 'lower right')

# The strings 'upper left', 'upper right', 'lower left', 'lower right' place the legend at the corresponding corner of the axes.

# The strings 'upper center', 'lower center', 'center left', 'center right' place the legend at the center of the corresponding edge of the axes.


plt.show()