# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:02:37 2024

@author: Louis_office
"""

from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

X,y=datasets.make_regression(n_samples=200,n_features=1,n_targets=1,noise=7)

plt.scatter(X,y)

plt.show()