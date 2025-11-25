# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 16:08:51 2025

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
plots = []
for i in range(5):
    for j in range(4):
        ax = plt.subplot2grid((5,4), (i,j))
        ax.scatter(range(20),range(20)+np.random.randint(-5,5,20))
plt.show()