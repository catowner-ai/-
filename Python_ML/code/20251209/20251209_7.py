# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:35:55 2024

@author: Louis_office
"""
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# temp_list=[29,28,34,31,25,29,32,31,24,33,25,31,26,30,32,33,34,32]#天氣溫度

temp=np.array([29,28,34,31,25,29,32,31,24,33,25,31,26,30,32,33,34,32]) #天氣溫度

print(type(temp))


black_tea_sales=np.array([77,62,93,84,59,64,80,75,58,91,51,73,65,84,82,86,90,85])  #紅茶x行 紅茶銷售杯數

print(type(black_tea_sales))

#%%


print(temp.shape)
print(black_tea_sales.shape)


temp_2d=np.reshape(temp,(len(temp),1))  # 把temp 1維的資料轉成2維


print("*************")
print("temp_2d.shape = ",temp_2d.shape)

print("*************")
print("temp_2d data = " ,temp_2d)


black_tea_sales_2d=np.reshape(black_tea_sales,(len(black_tea_sales),1))  # 把black_tea_sales 1維的資料轉成2維


print("*************")
print("black_tea_sales_2d.shape = ",black_tea_sales_2d.shape)

print("*************")
print("black_tea_sales_2d data = ",black_tea_sales_2d)


# print(temp_2d.shape)
# print(black_tea_sales_2d.shape)

# print(temp_2d)
# print(black_tea_sales_2d)

#以上為資料的整理

#%%

#機器學習的開始
lm = LinearRegression()


print(np.reshape(temp,(len(temp),1)))
print(np.reshape(black_tea_sales,(len(black_tea_sales),1)))        


# 第一種學習方式
# lm.fit(temp_2d,black_tea_sales_2d)



# 第二種學習方式
lm.fit(np.reshape(temp,(len(temp),1)),np.reshape(black_tea_sales,(len(black_tea_sales),1)))





print(lm.coef_)
print(lm.intercept_)


#以上就是線性迴歸機器學習完成

#%%  new temp to predict

#lm_predicted
#new temp predict
predicted_temp = np.array([30,26,35,45,29,25,33,28,20,19,41])

predicted_sales=lm.predict(np.reshape(predicted_temp,
                                      (len(predicted_temp),1)))
#sales
print(predicted_sales)





#%%  draw scatter plot

plt.scatter(temp,black_tea_sales,color='black')
plt.plot(temp,lm.predict(np.reshape(temp,
                                      (len(temp),1))),color='blue',linewidth=3)
plt.plot(predicted_temp,predicted_sales,color='red',marker='^',markersize=10)

plt.xticks(())
plt.yticks(())
plt.show()



#%%  mse & R平方

mse=np.mean((lm.predict(temp_2d)-black_tea_sales_2d)**2)
r_squared=lm.score(temp_2d,black_tea_sales_2d)

print(mse)
print(r_squared)


#R 平方，也稱為決定係數，是回歸分析中使用的統計度量，用於評估模型與觀測數據的擬合優度 (愈接近1愈好)


#%%  // 20240827 

predicted_sales=lm.predict(temp_2d)

print("*********")

print(predicted_sales)

print("r2_score",r2_score(black_tea_sales,predicted_sales))






