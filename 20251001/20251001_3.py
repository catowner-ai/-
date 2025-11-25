# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:11 2024

@author: Louis_office
"""

import pandas as pd


#%%

df=pd.read_csv('Data_set/NBA.csv')

print(df.head(5))
print("**********************")
print(df.tail(10))


print("******** info *********")
print(df.info())

print("******** shape *********")

print(df.shape)

#%%

#方法一
salary_data=df["Salary"]
print(salary_data)

print("******** salary_data_data_type *********")
print(type(salary_data))
      
#方法二
print(df["Salary"])

#%% 範圍取內容一


# #方法一
# print(df["Name"][10:15])



# #方法二
print(df["Name"].head(10))


#方法三
Name_data=df["Name"]
print("******** Name_data_data_type *********")
print(type(Name_data))
print(Name_data.head(10))






#%% 範圍取內容二(中間區域)

print(df["Name"][20:30])

#%% 二個欄位以上範圍取內容

print(df[["Name","Salary"]][20:30])

print(df[["Name","Salary","Team"]][1:20])


#%%

print(df.info())

print("******after insert Sport Column******")

df.insert(3,column="Sport",value="Basketball")

print(df.info())


#%%

NBA_df=pd.read_csv('Data_set/NBA.csv')

print(NBA_df)

print(NBA_df.info())

print("******after dropna ******")

NBA_newdf=NBA_df.dropna()

print(NBA_newdf)

print(NBA_newdf.info())



#%%

NBA_df2=pd.read_csv('Data_set/NBA.csv')

print(NBA_df2)

print(NBA_df2.info())


print("******after fillna ******")


NBA_newdf2=NBA_df2.fillna(50)

print(NBA_newdf2.info())

#%%

NBA_df3=pd.read_csv('Data_set/NBA.csv')

print(NBA_df3.sort_values("Name"))


print("******origin data NBA_df3 ******")

print(NBA_df3)

print("******sort_value NBA_df3_sort ******")

NBA_df3_sort=NBA_df3.sort_values("Name")
print(NBA_df3_sort)


#%%
NBA_df4=pd.read_csv('Data_set/NBA.csv')

print(NBA_df4.sort_values("Salary"))


NBA_Salary_sort=NBA_df4.sort_values("Salary")

print(NBA_Salary_sort)




NBA_Salary_sort_inverse=NBA_df4.sort_values("Salary",ascending=False)

print(NBA_Salary_sort_inverse)


#%%

NBA_Salary_sort_inverse.to_csv("NBA_Salary.csv")

NBA_Salary_sort_inverse.to_csv("Data_set/NBA_Salary.csv")
