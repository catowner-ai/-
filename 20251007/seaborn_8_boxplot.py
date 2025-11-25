# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:43:30 2023

@author: OfficePC
"""

'''
boxplot（箱線圖）是一種用作顯示一組資料分散情況的統計圖。
它能顯示出一組資料的最大值、最小值、中位數及上下四分位數。因形狀如箱子而得名。
這意味著箱線圖中的每個值對應於資料中的實際觀察值。
'''

import seaborn as sns
import matplotlib.pyplot as plt
titanic=sns.load_dataset('titanic')

print(titanic.info())

# sns.boxplot(x='class',y='age',data=titanic)

sns.boxplot(x='class',y='age',hue='who',data=titanic)

# sns.boxplot(x='age',y='class',hue='who',data=titanic)


# %%




# # 調整'order' 和 'hue_order' 參數，可以控制x軸順序。
fig,axes=plt.subplots(1,2) 

sns.boxplot(x='class',y='age',hue='who',
                    data=titanic,ax=axes[0])

sns.boxplot(x='class',y='age',hue='who',data=titanic,
            
                    order=['Third','Second','First'],
                    hue_order=['child','woman','man'],ax=axes[1])

# %%



sns.boxplot(x='class',y='age',hue='who',
                    linewidth=3,data=titanic)

