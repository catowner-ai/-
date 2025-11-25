# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:45:51 2023

@author: OfficePC
"""

'''
箱線圖與核密度圖的結合
箱線圖展示了分位數的位置
小提琴圖則展示了任意位置的密度，
通過小提琴圖可以知道哪些位置的密度較高。
在圖中，白點是中位數，黑色盒型的範圍是下四分位點到上四分位點，細黑線表示須。外部形狀即為核密度估計。
與箱線圖進行對比，以'titanic'資料集為例

'''

import seaborn as sns
import matplotlib.pyplot as plt
titanic=sns.load_dataset('titanic')

# sns.violinplot(x='class',y='age',data=titanic)



# sns.violinplot(x='class',y='age',hue='who',data=titanic)

# # hue參數只有兩個級別時，也可以通過設置'split'參數為True，“拆分”小提琴，提琴兩邊分別表示兩個分類的情況。
# sns.violinplot(x='class',y='age',hue='alive',
                data=titanic,split=True)

# # 在小提琴內部添加圖形來説明其進行分析，控制'inner'參數。
sns.violinplot(x='class',y='age',hue='alive',
                    data=titanic,split=True,inner='stick')



# #散點圖加入小提琴圖中。

sns.violinplot(x='class',y='age',data=titanic,inner=None)
sns.swarmplot(x='class',y='age',data=titanic,hue='who',color='green')
