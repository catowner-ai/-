# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:06:22 2022

@author: OfficePC
"""

import matplotlib.pyplot as plt
import seaborn as sns;sns.set() #還原成初始風格
import numpy as np

rng=np.random.RandomState(1)  #種子編號

x=10*rng.rand(50)


# y=3*x-5+rng.randn(50)
# plt.scatter(x,y)



# y2=6*x-5+rng.randn(50)
# plt.scatter(x,y2)



# y3=9*x-5+rng.randn(50)
# plt.scatter(x,y3)


y4=9*x+5+rng.randn(50)
plt.scatter(x,y4)


#%%



from sklearn.linear_model import LinearRegression

LR_model = LinearRegression(fit_intercept=True)


print(x)
print(type(x))


print("*************")
print(x[:,np.newaxis]) # x 轉二維的資料
print("*************")

print(x)
print(type(x))

#  LR_model training ok
LR_model.fit(x[:,np.newaxis],y4) #LinearRegression . fit ok

#%%

##接下來程式是做測試用
xfit=np.linspace(0,10,10) #測試用數據
print(xfit)

print(xfit[:,np.newaxis]) # xfit 轉二維的資料

yfit=LR_model.predict(xfit[:,np.newaxis])  #做預測


plt.scatter(x,y4)


plt.plot(xfit,yfit)


print("Model slope",LR_model.coef_[0])
print("Model intercept:",LR_model.intercept_)
