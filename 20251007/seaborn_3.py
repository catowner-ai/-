# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:17:17 2023

@author: OfficePC
"""
'''
heatmap()
sns.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g', annot_kws=None, linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False, xticklabels='auto', yticklabels='auto', mask=None, ax=None, **kwargs)
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib
flights_df = sns.load_dataset('flights')
#f=flights_df.pivot('year','month','passengers') 會報錯
f = flights_df.pivot(index='year', columns='month', values='passengers')

sns.heatmap(f)