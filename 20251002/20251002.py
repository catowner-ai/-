# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:42:15 2024

@author: Louis_office
"""
import pandas as pd

#%%
nba=pd.read_csv('Data_set/NBA.csv')


print(nba.info())



#%%
print(nba.describe())



# method 1 find Team column data
print(nba['Team'])

print(nba[['Team','Salary']])

print(nba['Team'][:11])

# method 2 find Team column data
print(nba.Team)

# print(nba.[Team,Salary])

# print(nba.Team[:11])


#%%


nba_team=nba["Team"]


x=nba["Team"]=="Los Angeles Lakers"


#方法一 挑出只有Los Angeles Lakers的資料
print(nba[x])

nba_NYK=nba[nba["Team"]=="New York Knicks"]


#%%
#Los Angeles Lakers的薪水加總輸出 (分解動作)
print(nba[nba["Team"]=="Los Angeles Lakers"][["Name","Salary"]])

Los_Angeles_Lakers_Salary=nba[nba["Team"]=="Los Angeles Lakers"]["Salary"]

print(Los_Angeles_Lakers_Salary.sum())
   

    



#一次性完成Los Angeles Lakers的薪水加總輸出
print(nba[nba["Team"]=="Los Angeles Lakers"]["Salary"].sum())

#%%


#方法二 挑出只有Los Angeles Lakers的資料
Team_filter=(nba["Team"]=="Los Angeles Lakers")


print(nba[Team_filter])


# #method 1 
Los_Angeles_Lakers_Team=nba[Team_filter]


#method 2
# Los_Angeles_Lakers_Team=nba[nba["Team"]=="Los Angeles Lakers"]


print(Los_Angeles_Lakers_Team)
print(Los_Angeles_Lakers_Team.sort_values("Salary",ascending=False))



New_York_Knickss_Team=nba[nba["Team"]=="New York Knicks"]


#%%

# Team_filter=(nba["Team"]=="Los Angeles Lakers")
# Los_Angeles_Lakers_Team=nba[Team_filter]

Los_Angeles_Lakers_Team=nba[nba["Team"]=="Los Angeles Lakers"]
print(Los_Angeles_Lakers_Team)



# find Salary >=7000000 (method1)
Los_Angeles_Lakers_salary_mask = Los_Angeles_Lakers_Team["Salary"]>=7000000
Los_Angeles_Lakers_Team_Salary=Los_Angeles_Lakers_Team[Los_Angeles_Lakers_salary_mask]
print(Los_Angeles_Lakers_Team_Salary)


#%%

#找出全聯盟薪水大於7000000的資料方法一
nba_salary_mask=nba["Salary"]>=7000000
nba_Salary_result=nba[nba_salary_mask]
print(nba_Salary_result)


#找出全聯盟薪水大於7000000的資料方法二
nba_Salary_result=nba[nba["Salary"]>=7000000]
print(nba_Salary_result)


NY_salary_mask=New_York_Knickss_Team["Salary"]>=7000000
NY_salary_data=New_York_Knickss_Team[NY_salary_mask]
print(NY_salary_data)



# # find Salary >=7000000 (method2)
# Los_Angeles_Lakers_Team_Salary=Los_Angeles_Lakers_Team[Los_Angeles_Lakers_Team["Salary"]>=7000000]
# print(Los_Angeles_Lakers_Team_Salary)


# nba_Salary_result=nba[nba["Salary"]>=7000000]
# print(nba_Salary_result)



#%%


x1=New_York_Knickss_Team["Salary"]>=7000000

x2=(New_York_Knickss_Team["Salary"]<=10000000)

#位元處理 &   --> 1&1 -->1  0&1-->0  1&0-->0  0&0-->0  (1表True 0表False)
#邏輯處理and 判斷是或否  是 and 是 -->結果為　＝＝＞　是　　(而True（是） 　　－－＞值是非０都算True)　


NY_salary_mask=(New_York_Knickss_Team["Salary"]>=7000000) & (New_York_Knickss_Team["Salary"]<=10000000)
NY_salary_data=New_York_Knickss_Team[NY_salary_mask]
print(NY_salary_data)




#%%
Los_Angeles_Lakers_Team_Salary=Los_Angeles_Lakers_Team[Los_Angeles_Lakers_Team["Salary"].between(7000000,16000000)]

print(Los_Angeles_Lakers_Team_Salary)


New_York_Knickss_Team_Salary=New_York_Knickss_Team[New_York_Knickss_Team["Salary"].between(7402812,8000000)]

print(New_York_Knickss_Team_Salary)

#%%


#step 1 找出Philadelphia_76ers資料
Philadelphia_76ers=nba[nba["Team"]=="Philadelphia 76ers"]
print(Philadelphia_76ers)



#step 2 再找出Philadelphia_76ers資料裡薪水介於5000000 --> 10000000
# find Salary 5000000 --> 10000000(method2)
Philadelphia_76ers_Salary=Philadelphia_76ers[Philadelphia_76ers["Salary"].between(5000000,10000000)]
print(Philadelphia_76ers_Salary)



#%%

#step 1 找出Utah_Jazz資料
Utah_Jazz=nba[nba["Team"]=="Utah Jazz"]
print(Utah_Jazz)



#step 2 再找出Utah_Jazz資料裡Age介於25--> 35
Utah_Jazz_Age=Utah_Jazz[Utah_Jazz["Age"].between(25,35)]
print(Utah_Jazz_Age)


#%%


#過濾條件一
mask1=nba["Team"]=="Philadelphia 76ers"

mask1_1=nba["Team"]=="Los Angeles Lakers"



# Philadelphia_76ers_Salary_Filter

#過濾條件二
mask2=nba["Salary"].between(5000000,10000000)

#同時滿足過濾條件一 與 過濾條件二
Philadelphia_76ers_Salary_Filter=nba[mask1 & mask2 ]

print(Philadelphia_76ers_Salary_Filter)




#Philadelphia_76ers__Los_Angeles_Lakers_Salary_Filter

Philadelphia_76ers__Los_Angeles_Lakers_Salary_Filter=nba[(mask1|mask1_1) & mask2 ]

print(Philadelphia_76ers__Los_Angeles_Lakers_Salary_Filter)


#%%

print(nba.Salary)

#method 1
print(nba.Salary.max())

#method 2
print(nba['Salary'].max())

print(nba.sort_values('Salary',ascending=False).head(5))

#%%

print(nba.describe())

print(nba.Salary.min())

print(nba.Salary.mean())   # 平均值

print(nba.Salary.std())     #標準差

print(nba.Salary.count())   #資料筆數

print(nba.Salary.median())  #中位數

#%%

# and ，or  邏輯運算 
# & , |     二進制運算(位元運算)

a=5
b=10

print(a and b)  # true 


print(a | b) # 0101 
            #  1010 | 
            #---------
            #  1111
          #    0011 &
            # --------
           #   0011



