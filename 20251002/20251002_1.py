# -*- coding: utf-8 -*-
"""


@author: OfficePC
"""

# 
import pandas as pd
data_path ='data/chipotle.tsv'


try:    
chipo = pd.read_csv('data/chipotle.tsv', sep='\t')

print(chipo.info())

print(chipo.describe())



#%%

print(chipo.item_price)


# 將item_price轉換為數值型態
chipo.item_price = chipo.item_price.apply(lambda y: float(y[1:]))

print(chipo.info())
print(chipo.head())



#%%

 # 0   order_id            4622 non-null   int64 
 # 1   quantity            4622 non-null   int64 
 # 2   item_name           4622 non-null   object
 # 3   choice_description  3376 non-null   object
 # 4   item_price          4622 non-null   object

print(chipo.item_name)

x=chipo.groupby(['item_name'])
print(x.sum())

y=x.sum()


# 查詢最受歡迎的食物
data=chipo.groupby(['item_name']).sum().sort_values('quantity', ascending=False)
print(data)

# 查詢此餐廳有多少種商品
item_count=chipo.groupby(['item_name']).sum().sort_values('quantity', ascending=False).count()
print(item_count)

# 查詢此餐廳有多少種商品
item_count2=chipo.groupby(['item_name']).sum().count()
print(item_count2)


#%%

# 刪除order_id欄 並找出賣最好的前十筆資料
favoriteItems=data.drop('order_id', axis=1)
print(favoriteItems.head(10))

#%%

# 查詢最受歡迎的食物
favoriteItems2 = chipo.groupby(['item_name']).sum().sort_values('quantity', ascending=False)
print(favoriteItems2)



favoriteItems3 = chipo.groupby(['item_name']).agg({'order_id' : 'count', 'quantity' : 'sum', 'item_price' : 'sum'}).sort_values('quantity', ascending=False)
print(favoriteItems3.head(10))



#%%
#各別訂單編號的數量
print(chipo.order_id.value_counts())

#總訂單數
print(chipo.order_id.value_counts().count())


#總收入 / 總訂單數   --> 每一單的比均收入
print(chipo.item_price.sum() / chipo.order_id.value_counts().count())


# chipo.groupby(by=['order_id']).sum()['item_price'].mean()