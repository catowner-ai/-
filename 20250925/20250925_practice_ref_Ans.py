# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 09:11:41 2025

@author: USER
"""


# Stu_profile=[["apple",80,90,80,75,80],["louis",80,90,70,80,60]]

Stu_profile=[]

Stu_data_temp=[]

Stu_data_list=["name","chi","eng","math","soci","nat"]

stu_num=int(input("請輸入有幾位同學的分數要輸入"))  #2

# print(stu_num)

for i in range(stu_num):  #0-1
    Stu_data_temp.clear()
    score_sum=0
    score_avg=0
    print("請輸入第",i+1,"位同學的資料")
    for j in range(len(Stu_data_list)):  #0--5
        Stu_data_temp.append(input("請輸入"+Stu_data_list[j]+"-->"))
        if j>=1:
            score_sum+=float(Stu_data_temp[j])  #a=a+b
    score_avg=score_sum//5   
    Stu_data_temp.append(score_sum) 
    Stu_data_temp.append(score_avg) 
    
    print(Stu_data_temp)
    
    
    ## 方法一 (小問題)
    # Stu_profile.append(Stu_data_temp)
    # print(Stu_profile)  
    
    # # 方法二 (正常執行)
    stu_data=Stu_data_temp.copy()   
    Stu_profile.append(stu_data)
    
    # # 方法三 (小問題)
    # Stu_profile.extend(Stu_data_temp)
    # print(Stu_profile)  
   
    
#請用上面方法二的方式來執行   
# print(Stu_profile)
for i in range(stu_num): #0-1
    print("第",i+1,"位同學的資料為")
    for j in range(len(Stu_data_list)):
        print(Stu_data_list[j],"=",Stu_profile[i][j])
    print("總分",Stu_profile[i][6])
    print("平均",Stu_profile[i][7])
    
#%%



Stu_profile=[]

Stu_data_temp=[]

# Stu_data_list=["name","chi","eng","math","soci","nat"]

Stu_data_list=["name","chi","eng","math","soci","nat","sum","avg"]

stu_num=int(input("請輸入有幾位同學的分數要輸入"))

# print(stu_num)

for i in range(stu_num):
    Stu_data_temp.clear()
    score_sum=0
    score_avg=0
    print("請輸入第",i+1,"位同學的資料")
    for j in range(len(Stu_data_list)):
        if j<6:
            Stu_data_temp.append(input("請輸入"+Stu_data_list[j]+"-->"))
            if j>=1:
                score_sum+=float(Stu_data_temp[j])
        elif j==6:
            Stu_data_temp.append(score_sum)
        elif j==7:
            score_avg=score_sum//5
            Stu_data_temp.append(score_avg) 
        
        
    # score_avg=score_sum//5   
    # Stu_data_temp.append(score_sum) 
    # Stu_data_temp.append(score_avg)     
    # print(Stu_data_temp)
   
    # Stu_profile.append(Stu_data_temp)
    
    stu_data=Stu_data_temp.copy()   
    Stu_profile.append(stu_data)
    
    # Stu_profile.extend(Stu_data_temp)
    # print(Stu_profile)
    
     
# print(Stu_profile)
for i in range(stu_num):
    print("第",i+1,"位同學的資料為")
    for j in range(len(Stu_data_list)):
        print(Stu_data_list[j],"=",Stu_profile[i][j])
    # print("總分",Stu_profile[i][6])
    # print("平均",Stu_profile[i][7])