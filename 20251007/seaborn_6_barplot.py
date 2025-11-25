# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:34:51 2023

@author: OfficePC
"""

import seaborn as sns
import matplotlib.pyplot as plt


#導入資料集'titanic'，命名為'titanic'
titanic=sns.load_dataset('titanic')

#將'class'設為x軸，'survived'為y軸，傳入'titanic'數據
# sns.barplot(x='class',y='survived',data=titanic)



# 'hue'參數，對x軸的資料進行細分，細分的條件就是'hue'的參數值， x軸將其按'sex'（性別）再進行細分。

# sns.barplot(x='class',y='survived',data=titanic)

sns.barplot(x='class',y='survived',hue='sex',data=titanic)


#%%

# x軸設為'embarked'，y軸設為'survived'，並用'class'進行細分。
sns.barplot(x='embarked',y='survived',
                    hue='class',data=titanic)
