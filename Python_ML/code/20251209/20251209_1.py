# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:18:29 2024

@author: Louis_office
"""

from sklearn import datasets
import pandas as pd

iris_datasets=datasets.load_iris() #抓出datasets裡的iris資料

print(type(iris_datasets)) #datasets裡的iris資料格式

print(type(iris_datasets.data))# 印出四欄位資料型態

print(type(iris_datasets.target))# 印出目標結果資料型態

#%%

print(type(iris_datasets.feature_names))# 印出四欄位名稱資料型態
print(type(iris_datasets.target_names))# 印出目標欄位名稱資料型態


print(iris_datasets.feature_names)  # 印出四欄位名稱
print(iris_datasets.data)  # 印出四欄位內容


print(iris_datasets.target_names)  # 印出目標(結果)欄位名稱
print(iris_datasets.target)  # 印出目標(結果)欄位的內容



#%%

iris_feature_df=pd.DataFrame(iris_datasets.data,columns=iris_datasets.feature_names)
print(iris_feature_df)

print(iris_datasets.target)
      

iris_feature_df.loc[:,"flower_class"]=iris_datasets.target

iris_df=iris_feature_df

# print(iris_df)

print(iris_df.head())
