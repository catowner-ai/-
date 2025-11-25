# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:57:41 2023

@author: OfficePC
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib as mpl
from cycler import cycler

# matplotlib font path
# matplotlib\mpl-data\fonts\ttf
# ref : https://daxpowerbi.com/%E5%A6%82%E4%BD%95%E5%9C%A8win-10%E8%A7%A3%E6%B1%BAmatplotlib%E4%B8%AD%E6%96%87%E9%A1%AF%E7%A4%BA%E7%9A%84%E5%95%8F%E9%A1%8C/

#ref : https://matplotlib.org/stable/tutorials/introductory/customizing.html
#ref :https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html
# 指定預設字體

mpl.rcParams['font.sans-serif'] = ['SimHei']  

# 解決保存圖像是負號'-'顯示為方塊的問題 
mpl.rcParams['axes.unicode_minus'] = False  













