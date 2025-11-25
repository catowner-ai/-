# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:26:46 2022

@author: OfficePC
"""
import numpy as np
import matplotlib.pyplot as plt

plt.xlabel("Age")
plt.ylabel("Monthly Salary")

#年紀數據重新編碼
# age_data=[15,22,35,46,21,6] --> [1,2,3,4,2,1]

#薪水數據重新編碼
# Salary_data =[28000,36000,42000,24000,17000,10000]   --> [2,3,3,1,1,1]

plt.xticks(np.arange(7),("","<=20","21-30","31~40","41~50",">=51",""))

plt.yticks(np.arange(6),("","<25k","25k~35k","35k~45k",">45k",""))
# plt.minorticks_on()



x=np.array([1,2,3,4])
y=x+0.5


plt.plot(x,y,'ro')
plt.show()


