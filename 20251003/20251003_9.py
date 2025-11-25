# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:47:25 2022
@author: OfficePC
"""
# plot(x, y, color='green', marker='o', linestyle='dashed',
#      linewidth=2, markersize=12)

# ref : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
# ref : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=x*2


plt.figure(num=5,figsize=(6,4),facecolor="lightblue")
plt.plot(x,y,"ro", linestyle='dashed',linewidth=3, markersize=12)
plt.show()





#%%
plt.figure(num=6,figsize=(6,4),facecolor="cyan")
plt.plot(x,y,"bo")
plt.plot(x+2,y+2,"go")
plt.show()



#%%
plt.figure(num=7,figsize=(6,4),facecolor="cyan")
plt.plot(x,y,"ro")
plt.plot(x+2,y+2,"yo")
plt.show()









