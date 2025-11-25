# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:39:09 2023

@author: OfficePC
"""

import seaborn as sns
import matplotlib.pyplot as plt
titanic=sns.load_dataset('titanic')

# sns.countplot(x='deck',data=titanic)

# sns.countplot(x='deck',hue='sex',data=titanic)

# 調換橫縱坐標，也就是類別放於縱坐標，計數值橫坐標顯示，將x軸換為y軸即可。
# sns.countplot(y='deck',hue='who',data=titanic)

sns.countplot(y='deck',hue='who',data=titanic)