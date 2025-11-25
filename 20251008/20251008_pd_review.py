
import numpy as np
import pandas as pd



# pd.read_csv(filename)   #載入csv
# pd.read_table(filename) # 載入有分隔符號的(如TSV) 中的資料
# pd.read_excel(filename) #載入excel
# pd.read_sql(query, connection_object) # 載入SQL資料表/資料庫中的資料
# pd.read_json(json_string) # 載入JSON格式的字元，URL位址或者檔中的資料
# pd.read_html(url) # 載入經過解析的URL位址中包含的資料框 (DataFrame) 資料
# pd.DataFrame(dict)  # 載入Python字典 (dict) 裡面的資料，其中key是資料框的表頭，value是資料框的內容。


#step1
# df=pd.read_csv("apple.csv")   






#%%

pd.DataFrame(np.random.rand(5, 10)) 
# 建立一個5列10行的由隨機浮點數組成的DataFrame

# pd.Series(my_list) #物件 my_list 中建立一個資料組


my_list = ['abc',123,'HelloWorld', 5.7]
pd.Series(my_list)


df = pd.DataFrame(np.random.rand(10, 5))

df.index = pd.date_range('2025/10/1', periods=df.shape[0])
print(df)


#%%


# df.head(n)  # 查看前n行的資料
# df.tail(n)  # 查看後n行的資料

df = pd.DataFrame(np.random.rand(100, 5))
print(df.head(5))

df = pd.DataFrame(np.random.rand(100, 5))
print(df.tail(8))

print(df.shape) # 查看資料的形狀（列和欄）




#%%

# df.info() # 查看資料的索引、資料類型及記憶體資訊

print(df.info())

# df.describe() # 對於資料類型為數值型的列，查詢其描述性統計的內容

print(df.describe() )



#%%
# s.value_counts(dropna=False) # 查詢每個唯一資料值出現次數統計

s = pd.Series([1,2,3,3,4,np.nan,5,5,5,6,7])
print(s)

print(s.value_counts(dropna=True))



s = s.apply(lambda x: x+1*2)
print(s)


#透過Series裡的value_counts功能來查詢data frame 每個列的唯一資料值出現次數統計
df.apply(pd.Series.value_counts) # 查詢資料框 (Data Frame) 中每個列的唯一資料值出現次數統計



#%%
# df[col] # 以陣列 Series 的形式返回選取的列


df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))

print(df['C'])


# df[[col1, col2]] # 選擇多列

df = pd.DataFrame(np.random.rand(5, 5), columns=list('ABCDE'))

print(df[['C', 'D']])


#%%

# s.loc['index_one'] # 按索引選取

s = pd.Series(np.array(['I', 'Love', 'Taiwan']))
s.loc[1]



#%%
# df.DataFrame[n, :] #選取第n行

df = pd.DataFrame(np.array([['I', 'Love', 'Taiwan'], ['I', 'Love', 'Data']]))
print(df)

print(df.iloc[1, :])


# df.iloc[0, 0] # 選取第一個元素

df = pd.DataFrame(np.random.rand(5, 5))
print(df)

print(df.iloc[2, 1])



#%%


# df.columns = ['a', 'b'] # 對欄位名稱重新命名

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                   'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                   'C':np.array([1,np.nan,2,3,6,np.nan]),
                   'D':np.array([1,np.nan,2,3,6,np.nan]),
                   'E':'foo'})
print(df)


df.columns = ['q', 'w', 'e', 'R', 'T']
print(df)



#%%
# pd.isnull() # 檢查資料中出現空值的情況, 返回一個布林型的列
# pd.notnull() #相對應isnull 返回不是空值的情況


df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                   'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                   'C':'foo'})
print(df)

print(df.isnull())

print(df.info())


# df.isnull().sum() # 對每一列的空值進行統計
print(df.isnull().sum())


#%%
# df.dropna(axis = 0, thresh=n) # 刪除包含空值的列  axis = 1時刪除欄  # thresh = n移除空值超過(包括等於)n的行

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                   'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                   'C':'foo'})
print(df)

print(df.dropna(axis = 0))

df1=df.dropna(axis = 0)

print("原始的df")
print(df)


print("刪除nan資料後的df")
print(df1)


print("原始的df")
print(df)
print(df.dropna(axis = 1))




#%%
df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                   'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                   'C':'foo'})

print(df)

#用平均值來填充空值 分解動作

df_A=df['A'].fillna(df['A'].mean()) # 用平均值來填充空值
print(df_A)




df_B=df['B'].fillna(df['B'].mean()) # 用平均值來填充空值
print(df_B)




print(df)
#把平均值處理後的結果，塞回原df的各別欄位

df['A']=df_A

df['B']=df_B

print(df)



# df['A']=df['A'].fillna(df['A'].mean()) # 用平均值來填充空值

# df['B']=df['B'].fillna(df['B'].mean()) # 用平均值來填充空值
#%%

df = pd.DataFrame({'A':np.array([1,np.nan,2,3,6,np.nan]),
                   'B':np.array([np.nan,4,np.nan,5,9,np.nan]),
                   'C':'foo'})

print(df)

#把平均值處理後的結果，塞回原df的各別欄位
df['A']=df['A'].fillna(df['A'].mean()) # 用平均值來填充空值
df['B']=df['B'].fillna(df['B'].mean()) # 用平均值來填充空值

df['A1']=df['A'].fillna(df['A'].mean())

print(df)

#%%


s = pd.Series([1,3,5,np.nan,7,9,9])
s.fillna(s.mean())


# s.astype(type) # 轉換資料型態類型


s = pd.Series([1,3,5,np.nan,7,9,9])
s.fillna(s.mean()).astype(int)




#%%
s.replace(1, 'one') # 將Series中的1替換為one

s = pd.Series([1,3,5,np.nan,7,9,9])
s.replace(1,'one')


s.replace([1,3],['one','three']) # 將陣列(Series)中所有的1替換為'one', 所有的3替換為'three'

s = pd.Series([1,3,5,np.nan,7,9,9])
s.replace([1,3],['one','three'])


#%%
# df.rename(columns=lambda x: x + 2) # 將全體欄重命名


df = pd.DataFrame(np.random.rand(4,4))
print(df)

df1=df.rename(columns=lambda x: x+ 2)


# df.columns = ['q', 'w', 'e']


# print(df)
print(df1)


df2=df.rename(columns={0: 'apple'}) # 將選擇的欄重命名
print(df2)



df2=df.rename(columns={0: 'banana',1: 'apple'}) # 將選擇的欄重命名
print(df2)


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))

print(df)

df=df.rename(columns={'A':'Apple', 'B':'Bnana'})

print(df)

#%%

df = pd.DataFrame(np.random.rand(4,6))
print(df)

print(type(df))

print(df.index)

print(df.columns)

print(df.dtypes)

print(df.values)


#%%
# df.set_index('column_one') # 改變索引


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df)


df1=df.set_index('B')
print(df1)

print(df)


#%%
# df.rename(index = lambda x: x+ 1) # 改變全體索引

df = pd.DataFrame(np.random.rand(10,5))
print(df)


# df_0=df.rename(columns=lambda x: x+2)
# print(df_0)


df2=df.rename(index = lambda x: 2025+x)
print(df2)


df3=df.rename(index = lambda x: "2025"+"-01-0"+str(x))
print(df3)


#%%

# df[df[col] > 0.5] # 選取資料df中對應行的數值大於0.5的全部列


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df)


print(df[df['A'] > 0.5])


print(df[(df['A'] > 0.5) & (df['B'] < 0.7)])


#%%
# df.sort_values(col, ascending=True) #按照列進行排序  # ascending: True 昇冪 False 降冪


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df)


print(df.sort_values('A', ascending=False))



# df.sort_values([col1,col2],ascending=[True,False]) # 按照資料框的列col1昇冪，col2降冪的方式對資料框df做排序

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df)

print(df.sort_values('A', ascending=True))


print(df.sort_values(['A','E'],ascending=[True,False]))



#%%
# groupby 分組

# df.groupby(col) # 按照某列對資料框df做分組 # 常與count進行連用，統計出各詞的個數


df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})

print(df)

print(df.groupby('B').count())


# df.groupby([col1,col2]) # 按照列col1和col2對資料框df做分組

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
print(df)

print(df.groupby(['A', 'B']).sum())

print(df.groupby('A').sum())


# df.groupby(col1)[col2].mean() # 按照列col1對資料框df做分組處理後，返回對應的col2的平均值


df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
print(df)

print(df.groupby('A').mean())  # 會出錯

print(df.groupby('A')['D'].mean())

print(df.groupby('A')['B'].count())

print(df.groupby('A')['C'].count())




print(df.groupby('A').agg({'B':'count', 'C':'count','D':'mean'}))




#%%
# df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) # 做透視表，索引為col1,針對的數值列為col2和col3，分組函數為平均值


df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})


df.pivot_table(df, index=['A', 'B'], columns=['C'], aggfunc=np.sum)


#%%


import numpy as np
import pandas as pd

df = pd.DataFrame({'A':np.array(['foo','foo','foo','foo','bar','bar']),
      'B':np.array(['one','one','two','two','three','three']),
     'C':np.array(['small','medium','large','large','small','small']),
     'D':np.array([1,2,2,3,3,5])})
print(df)

df_A=df.groupby('A')
print(df)


# print(df.groupby('A')['D'].mean())

print(df_A.D.mean())

#%%

# df.apply(np.mean, axis=0) # 對資料框df的每一欄求平均值 axis: 0對欄名（橫著的）進行處理  1對索引（豎著的）進行處理

df =pd.DataFrame(np.random(10,5),columns=list('ABCDE'))


df =pd.DataFrame(np.random.randint(0,10,size=(10,5)),columns=list('ABCDE'))

print(df)

df.apply(np.mean, axis=0)

df['A'].mean



#%%
#資料的連接(join)與組合(combine)

# df1.append(df2) # 在資料框df2的末尾添加資料框df1，其中df1和df2的列數應該相等  列合併


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

# df3=df1.append(df2)

# print(df3)


#%%
# pd.concat([df1, df2], axis=1) # 在資料框df1的列最後添加資料框df2,其中df1和df2的行數應該相等  # 中括弧可以換成圓括號  # axis: 0進行行合併  1進行列合併

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   )
df4=pd.concat([df1, df2], axis=0)
print(df4)



df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'E': ['A4', 'A5', 'A6', 'A7'],
                    'F': ['B4', 'B5', 'B6', 'B7'],
                    'G': ['C4', 'C5', 'C6', 'C7'],
                    'H': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 3])
df5=pd.concat((df1, df2), axis=1)
print(df5)

#%%
# df1.join(df2,on=col1,how='inner') # 對資料框df1和df2做內連接，其中連接的欄為col1

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],           
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key': ['K0', 'K1', 'K0', 'K1']})
   

df2 = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                     index=['K0', 'K1'])
df1.join(df2, on='key', how='inner')



#%%
# 資料的統計

# df.mean() # 得到資料框df中每一欄的平均值


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df)

print(df.mean())




#%%
# df.corr() # 得到資料框df中每一欄與其他欄的相關係數


print(df.corr())



#%%
df.count() # 得到資料框df中每一欄的非空值個數

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
# df.loc[0][0] = np.nan
df.iloc[0, 0] = np.nan
df.count()





#%%
# df.max() # 資料框df中每一欄的最大值

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df.max())


# df.min() # 資料框df中每一欄的最小值


df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df.min())


#%%
# df.median() # 資料框df中每一欄的中位數

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df.median())


#%%
df.std() # 資料框df中每一欄的標準差

df = pd.DataFrame(np.random.rand(10,5),columns=list('ABCDE'))
print(df.std())


#%%
# ### 資料的匯出

# df.to_csv(filename) # 將(DataFrame)中的資料匯出存在csv格式的檔中
# df.to_excel(filename) # 將 (DataFrame)中的資料匯出存在Excel格式的檔中
# df.to_sql(table_name,connection_object) # 將資料框 (DataFrame)中的資料匯出存在SQL資料表/資料庫中
# df.to_json(filename) # 將資料框 (DataFrame)中的資料匯出存在JSON格式的檔中

#step2
# df.to_csv("new_apple.csv") 
