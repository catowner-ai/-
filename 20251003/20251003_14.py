# # -*- coding: utf-8 -*-
# """
# Created on Fri Feb 24 21:33:26 2023

# @author: OfficePC
# """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores=[10,15,80,22,93,55,88,62,45,75,81,34,99,84,85,55,58,63,68,82,84]
bins=[0,10,20,30,40,50,60,70,80,90,100]


plt.hist(scores,bins,histtype="barstacked")

plt.xlabel("Scores")
plt.ylabel("Students")

plt.title("Student Score")
plt.show()






#%%


import numpy as np
import matplotlib.pylab as plt

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

data = [x1, x2, x3]


# 方法一
fig, ax = plt.subplots(3)
ax[0].hist(data, alpha=0.3, bins=40)
ax[1].hist(data, histtype='stepfilled', alpha=0.3, bins=40)
ax[2].hist(data, histtype='barstacked', alpha=0.3, bins=40)
plt.show()


#舊的設定值，2025年後不適用了
# ax[0].hist(data, alpha=0.3, normed=True, bins=40)
# ax[1].hist(data, histtype='stepfilled', alpha=0.3, normed=True, bins=40)
# ax[2].hist(data, histtype='barstacked', alpha=0.3, normed=True, bins=40)



# # 方法二
# fig, (ax,ax1,ax2) = plt.subplots(3)
# ax.hist(data, alpha=0.3, bins=40)
# ax1.hist(data, histtype='stepfilled', alpha=0.3, bins=40)
# ax2.hist(data, histtype='barstacked', alpha=0.3, bins=40)
# plt.show()