# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:40:37 2023

@author: OfficePC
"""

import seaborn as sns
import matplotlib.pyplot as plt
titanic=sns.load_dataset('titanic')

print(titanic.info())

# sns.stripplot(x='embarked',y='fare',data=titanic)

sns.stripplot(x='embarked',y='fare',data=titanic,jitter=0.3)



#%%

'''swarmplot() 防止它們重疊的演算法沿著分類軸調整點。
更好地表示觀測的分佈，適用較小的資料集。
'''
# sns.swarmplot(x='embarked',y='fare',data=titanic)

# 對散點圖添加更多細分的維度，Seaborn 中會以顏色來進行區分。
# sns.stripplot(x='embarked',y='age',hue='who',jitter=0.3,data=titanic)


sns.swarmplot(x='embarked',y='age',hue='who',data=titanic)