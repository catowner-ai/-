# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:22:40 2023

@author: OfficePC
"""
'''
Seaborn white / whitegrid / dark / darkgrid / ticks 幾種樣式，用 set_style() 函數控制，分別如下：
whitegrid 白色網格背景
white 白色背景（默認）
darkgrid 黑色網格背景
dark 黑色背景
ticks 四周帶有刻度的白色背景
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
sns.barplot(x=["A", "B", "C"], y=[100, 50, 300])



#%%




#建立一個20列6欄的資料
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2

# sns.boxplot(data=data)
# 設為白色網格背景
sns.set_style("whitegrid")
sns.boxplot(data=data)


# sns.set_style("ticks")
# sns.boxplot(data=data)
