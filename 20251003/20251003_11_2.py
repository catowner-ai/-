# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:50:57 2025

@author: USER
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f_data, ((ax_plot1,ax_plot2),(ax_plot3,ax_plot4),(ax_plot5,ax_plot6)) = plt.subplots(3, 2, sharex = False ,sharey=False,figsize=(10,6))
# print(f_data)


_, ((ax_plot1,ax_plot2),(ax_plot3,ax_plot4),(ax_plot5,ax_plot6)) = plt.subplots(3, 2, sharex = False ,sharey=False,figsize=(10,6))
#3列2欄

x = np.arange(0,5,1)
df_data1 =  pd.DataFrame(x)
df_data2 =  pd.DataFrame(x**2)
df_data3 =  pd.DataFrame(x**4)
df_data4 =  pd.DataFrame(x**6)
df_data5 =  pd.DataFrame(x**5)
df_data6 =  pd.DataFrame(x**7)


ax_plot1.plot(df_data1)
ax_plot2.plot(df_data2)
ax_plot3.plot(df_data3)
ax_plot4.plot(df_data4)
ax_plot5.plot(df_data5)
ax_plot6.plot(df_data6)
plt.show()