# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:55:05 2023

@author: OfficePC
"""

'''
seaborn 中的分類色板，主要用 color_palette() 函數控制，color_palette() 不寫參數則顯示為 Seaborn 預設顏色。

如果需要設置所有圖形的顏色，則用 set_palette() 函式定義。

Seaborn 中6個預設的顏色迴圈主題分別為： deep, muted, pastel, bright, dark, colorblind，下面我們列舉演示。
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#建立一個20列6欄的資料
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2


#sns.boxplot(data=data,palette=sns.color_palette('deep'))

sns.boxplot(data=data,palette=sns.color_palette('pastel'))

#%%

data2 = np.random.normal(size=(20, 10)) + np.arange(10) / 2  

#利用hls色彩空間進行調色
sns.boxplot(data=data2, palette=sns.color_palette('hls', 10))  
