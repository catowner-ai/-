# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:04:12 2023

@author: OfficePC
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib as mpl
from cycler import cycler

sns.set_context("notebook")
sns.lineplot(x=[0, 1, 2], y=[1, 3, 2])

#%%
#rc_ref:https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html

sns.set_context("notebook", rc={"lines.linewidth": 3})
sns.lineplot(x=[0, 1, 2], y=[1, 3, 2])

