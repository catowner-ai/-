# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:26:44 2023

@author: OfficePC
"""

#dataset_source
#  https://github.com/mwaskom/seaborn-data


#ref : https://blog.csdn.net/qq_41595507/article/details/107146256
#ref :　https://seaborn.pydata.org/tutorial/color_palettes.html
import seaborn as sns

import matplotlib.pyplot as plt
titanic_data=sns.load_dataset('titanic')


sns.palplot(sns.color_palette("Paired"))

print(type(titanic_data))
print(titanic_data)

print(titanic_data.info())




#%%

sns.barplot(x='sex',y='survived',data=titanic_data,palette=["#8446c2", "#ff7f0e"])

# sns.barplot(x='sex',y='survived',data=titanic_data,palette=sns.color_palette("Accent"))


#%%

titanic=sns.load_dataset('titanic')



#查看10筆隨機資料
print(titanic.sample(10))


#去除'age'中的遺漏值，distplot不能處理遺漏資料
sns.distplot(titanic['age'])

temp=titanic['age']

#%%

##去除'age'中的遺漏值，distplot不能處理遺漏資料
age1=titanic['age'].dropna()
sns.distplot(age1)



#去掉擬合的密度估計曲線
sns.distplot(age1,kde=False,color="b")


#%%
# 'bins'是控制分佈矩形數量的參數，可以增加其數量，看到更為豐富的資訊。
# 通過'bins'參數設定資料片段的數量
sns.distplot(age1,bins=30,kde=False)


#建立一個1列2欄的子圖,

fig,axes=plt.subplots(1,2)

#需要用axes[]表示是第幾張圖，從0開始
sns.distplot(age1,ax=axes[0]) #左圖
sns.distplot(age1,rug=True,ax=axes[1]) #右圖

#%%

#可以分別控制長條圖、密度圖的關鍵參數
fig,axes=plt.subplots(2,2) 

plt.subplots_adjust(wspace=0.5, hspace=0.5)

sns.distplot(age1,rug=True,ax=axes[0][0])


sns.distplot(age1,rug=True,
                     hist_kws={'color':'green','label':'hist'},
                     kde_kws={'color':'red','label':'KDE'},
                     ax=axes[0][1])


sns.distplot(age1,rug=False,ax=axes[1][0])


sns.distplot(age1,rug=True,
                      hist_kws={'color':'blue','label':'hist'},
                      kde_kws={'color':'yellow','label':'KDE'},
                      ax=axes[1][1])

#%%
# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None

# left  = 0.125  # the left side of the subplots of the figure
# right = 0.9    # the right side of the subplots of the figure
# bottom = 0.1   # the bottom of the subplots of the figure
# top = 0.9      # the top of the subplots of the figure
# wspace = 0.2   # the amount of width reserved for blank space between subplots
# hspace = 0.2   # the amount of height reserved for white space between subplots