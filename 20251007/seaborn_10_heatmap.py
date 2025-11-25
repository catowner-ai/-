# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:50:26 2023

@author: OfficePC
"""

import matplotlib.pyplot as plt
import seaborn as sns

flights_df = sns.load_dataset("flights")
print(flights_df.head(10))

# 'year'為縱軸，'month'為橫軸，'passengers'的值為標準繪製熱力圖。
sns.set_context("notebook", rc={"lines.linewidth": 3})

f=flights_df.pivot(columns='year',index='month',values='passengers')

sns.heatmap(f)

#%%
sns.heatmap(f, annot=True,fmt="d")

#%%

# Seaborn 的調色板控制熱力圖顯示的顏色，
apple = sns.diverging_palette(50,20,sep=10,as_cmap=True)
sns.heatmap(f,cmap=apple,annot=True,fmt="d")

