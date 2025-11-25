# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 20:40:33 2023

@author: OfficePC
"""

import matplotlib.pyplot as plt
# plot a line, implicitly creating a subplot(111)
years=[1950,1960,1965,1970,1980,1985,1990,
       1995,2000,2005,2010,2015]

pops = [2.5,2.7,3.3,3,4.0,4.4,4.8,5.3,
        6.1,6.9,6.5,7.3]

deaths=[1.3,2.1,1.5,2.8,3.5,2.6,4.4,4.8,5.3,
        3.4,5.2,6.5]


# 子圖  --> 一張圖裡面要畫出多個數據呈現的圖。

# subplot (xyz)  -->x指的是要幾列的圖(看垂直有幾筆)，y指的是要幾欄的圖(看橫向有幾筆)

plt.figure(figsize=(10, 8))

plt.subplot(431)  #3列2欄
plt.plot(years,pops,color=(255/255,100/255,100/255))
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(436)
plt.plot(years,deaths,color=(255/255,100/255,100/255))

plt.subplot(433)
plt.plot(pops,deaths,color=(160/255,100/255,180/255))

plt.subplot(434)
plt.plot(pops,deaths,color=(160/255,100/255,180/255))

plt.subplot(435)
plt.plot(pops,deaths,color=(160/255,100/255,180/255))

# plt.subplot(4312)
# plt.plot(pops,deaths,color=(160/255,100/255,180/255))


plt.subplot(4,3,12)
plt.plot(pops,deaths,color=(160/255,100/255,180/255))



plt.show()