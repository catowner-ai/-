# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:00:28 2023

@author: OfficePC
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib as mpl
from cycler import cycler

#建立一個20列6欄的資料
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2

plt.figure(figsize=(12, 6))

sns.boxplot(data=data,palette=sns.color_palette('Reds')) 

plt.savefig('red.png')
