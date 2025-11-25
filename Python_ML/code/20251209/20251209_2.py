# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:20:41 2024

@author: USER
"""

from sklearn import datasets

import matplotlib.pyplot as plt

X,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=3)

plt.scatter(X,y)

plt.show()