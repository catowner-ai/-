import matplotlib.pyplot as plt
import seaborn as sns

#sns.distplot()包含了matplotlib的hist()於sns.kdeplot()功能，
#增加了rugplot分佈(單個定量變量的數據圖)與
#scipy函式庫fit擬合參數分佈的用途
#https://seaborn.pydata.org/generated/seaborn.distplot.html

sns.distplot([10, 11, 12, 13, 14, 15])

plt.show()

#%%
import matplotlib.pyplot as plt
import seaborn as sns
#Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

#%%

'''直方圖：先分箱，然後計算每個分箱頻數的資料分佈，
和，橫條圖有空隙橫條圖的區別，直方圖沒有，橫條圖一般用於類別特徵，直方圖一般用於數位特徵（連續型）
多用於y值和數位（連續型）特徵的分佈畫圖
'''
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
import seaborn as sns 
sns.set()  #sns預設值

x=np.random.randn(100)
sns.distplot(x)

#%%
#通過hist和kde參數調節是否顯示直方圖及核密度估計(預設hist,kde均為True)
fig,axes=plt.subplots(1,3)  #建立一個1列3欄的圖片



sns.distplot(x,ax=axes[0])
sns.distplot(x,hist=False,ax=axes[1])  #不顯示直方圖
sns.distplot(x,kde=False,ax=axes[2])  #不顯示核密度




#bins：int或list，控制直方圖的劃分
#bins
fig,axes=plt.subplots(1,2) 
sns.distplot(x,bins=20,ax=axes[0]) #分成20個區間
sns.distplot(x,kde=False,bins=[x for x in range(4)],ax=axes[1]) 
#以0,1,2,3為分割點，形成區間[0,1],[1,2],[2,3]，區間外的值不計入

#%%



#rug：控制是否生成觀測數值的小細條
#rug
fig,axes=plt.subplots(1,2)
sns.distplot(x,rug=True,ax=axes[0]) #左圖
sns.distplot(x,ax=axes[1]) #右圖
#fit：控制擬合的參數分佈圖形，評估它與觀察資料的對應關係(黑色線條為確定的分佈)
#fit

#%%

from scipy.stats import *
sns.distplot(x,hist=False,fit=norm) #擬合標準常態分佈


#hist_kws, kde_kws, rug_kws, fit_kws參數接收字典類型，可以自行定義更多高級的樣式

sns.distplot(x,kde_kws={"label":"KDE"},vertical=True,color="y")

#norm_hist：若為True, 則直方圖高度顯示密度而非計數(含有kde圖像中預設為True)
#norm_hist
fig,axes=plt.subplots(1,2)
sns.distplot(x,norm_hist=True,kde=False,ax=axes[0]) #左圖
sns.distplot(x,kde=False,ax=axes[1]) #右圖

