# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:34:06 2024

@author: USER
"""

#查詢環境中有哪些字體可用

from matplotlib.font_manager import fontManager

for i in sorted(fontManager.get_font_names()):
    print(i)
    
    
#%%

#套用選擇好的字體

import matplotlib
matplotlib.rc('font', family='Microsoft YaHei')

#%%

import matplotlib.pyplot as plt

# plt.rcParams['axes.unicode_minus']=False  #負號呈現正常的語法

years=[1950,1960,1965,1970,1980,1985,1990,
       1995,2000,2005,2010,2015]


pops = [2.5,2.7,3.3,3,4.0,4.4,4.8,5.3,
        6.1,6.9,6.5,7.3]


plt.plot(years,pops)


plt.title("人口成長率")


plt.xlabel("人口成長率(每年)")
plt.ylabel("百萬人口")
plt.show()