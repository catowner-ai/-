# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:14:50 2023

@author: OfficePC
"""

# sns.dataset  --> href : https://github.com/mwaskom/seaborn-data

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib
flights_df = sns.load_dataset('flights')
print(flights_df)




flights_df = flights_df.pivot(index='month', columns='year', values='passengers')

print(flights_df)

#数据可视化：每年总乘客数
flights_df.sum().plot(kind="bar")

#flights_df.sum()：对每列（即每年）进行求和，表示每年所有月份的乘客总数。

#.plot(kind="bar")：绘制条形图（bar chart）

#✅ 输出图形：X 轴为年份，Y 轴为全年乘客总数。你会看到一个逐年上升的趋势，反映了航空出行的增长。

#%%
#sns

print(flights_df.sum().index)

print(flights_df.sum().values)

# sns.barplot(flights_df.sum().index,flights_df.sum().values)

sns.barplot(flights_df,x=flights_df.sum().index,y=flights_df.sum().values)