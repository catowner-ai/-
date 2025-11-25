# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:59:13 2024

@author: USER
"""

list1 = [] # list
 
tuple1 = () # tuple

print(type(tuple1))



#%%

# list2=[5,6,7,8,9,71.5,"abcde"] #list

tuple2 = (5,6,7,8,9,71.5,"abcde") # tuple

print(type(tuple2))

print(tuple2)

tuple2[3]=100  #不可行,tuple容器的資料是不可修改

#%%

f=(2,3,4,5)
g=()

h=(2,[3,4],(10,11,12))

x=f[1]
print(x)

y=f[1:3]

print(y)

z=h[1][1]

print(z)

h[1][0]=3   #　可以修改，list

print(h)

# h[2][0]=2000  #　不可以修改，tuple

# print(h)

# f=(2,3,4,5)
# g=()

# h=(2,[3,4],(10,11,12))


#%%

# f=(2,3,4,5)
# g=()

# h=(2,[3,4],(10,11,12))

# x=f[1]

print(y==h[1])  #tuple != list

print(y)
print(type(y))

print(h[1])
print(type(h[1]))


h[1].append(8)

print(h[1])

print(h)
#%%
h[1][0]=3   #　可以修改，list

print(h)

print(y==h[1])  #tuple != list
print(y)
print(type(y))

print(h[1])
print(type(h[1]))



#%%

data =(6,True,'XYZ',65.32)



x1,x2,x3,x4=data

print(x1)
print(x2)
print(x3)
print(x4)

#%%

datay =[6,True,'XYZ',65.32]
y1,y2,y3,y4=datay

print(y1)
print(y2)
print(y3)
print(y4)

print(type(y1))
print(y2)
print(y3)
print(y4)

y1=12.34
print(y1)

print(datay)


#%%

a,*b,c=(3.5,4,5,6,7)  #拆解出的資料只要是範圍-->就會變成list格式

print(type(a))
print(a)


print(type(b))
print(b)

print(type(c))
print(c)

#%%
a=(3.5,4,5,6,7)  #tuple

b=a[1:5]   #tuple  範圍取值  保留原資料型態

print(b)

print(type(b))


#%%
a1=[3.5,4,5,6,7]  #list

b1=a1[1:5]   #list 範圍取值  保留原資料型態 

print(b1)

print(type(b1))

b1[3]=100

print(a1)
print(b1)


#%%
x,*y,z,n,q=(5,6,7,8,9,10,12,"apple")  #拆解出的資料只要是範圍-->就會變成list格式

print(x)
print(y)
print(z)
print(n)
print(q)


#%%

a,*b=[3.5,4,5,6,7]                 #拆解出的資料只要是範圍-->就會變成list格式

print(type(a))
print(a)


print(type(b))
print(b)


#%%

xyz=set()

print(type(xyz))


xyz.add(1)

xyz.add(100)

xyz.add("louis")

xyz.add(200)

xyz.add(12.256)

xyz.add("apple")

xyz.add(45.263)

xyz.add(False)

xyz.add(20.256)

print(xyz)

print(1000 in xyz)


# x2=[1,2,3,4]  # list
# x3=(1,2,3,4)  #tuple

x1={1,"a","b",2,33,44,"abc"} # set


x2={1,"a",2,"b",33,44,"abc"}


print(x1==x2)

print(x1)

print(x2)






#%%

s1={3,3,3,3,5,7,8,3,5,4,6,2,8,1,1,1,1}

s2={3,5,6,4,3,7,2,1,5,4,7,5,3,3,4,5,8}

s3={0}

print(type(s3))

s3=s1

print(s1)

print(s2)

print(s1==s2)

print(s1 is s2)

print(id(s1))

print(id(s2))

print(id(s3))

print(s1 is s3)

print(s3)

print(s1==s3)

s3=s2

print(s1 is s3)
print(s1==s3)


print(s2 is s3)

# s1[2]=500  #無順序性!不能用index的方式[]來改值

s3=s1
s1.add(2000)

print(s1)
print(s3)

s3.add(0.254)

print(s1)
print(s3)



#%%


S={'B','A','C','D','E','B','A','C','D'}

print(len(S))

print(max(S))

print(min(S))



s5={3,3,3,3,3,5,5,7,8,3,5,4,6,2,8,1,1,1,1}

print(sum(s5))

#%%

s6={3,3,3,3,3,5,5,7,8,3,5,4,6,2,8,1,1,1,1}
s7={22,33,44,55}

print(55 in s7)


# s8=s6+s7

# s9=5*s6

#%%

#list 

Stu_list=["louis",18,"male",89,75,89,87,89]

print(Stu_list[0])


#dict
Stu_dict={"name":"louis","age":18,"sex":"male","chi":89,"Eng":75,"math":88,"soci":89,"natu":89}
           #key : value , #key : value
                  
print(Stu_dict["name"]) 
print(Stu_dict["age"]) 
print(Stu_dict["sex"]) 
print(Stu_dict["Eng"]) 
      

#%%

d1={"a":100,"b":500,"c":1000}

print(type(d1))

print(len(d1))

x1=d1["c"]

print(x1)

#%%


tt={}

print(type(tt))  # dict


s1={0,1,2,3}  #set

d11={"a1":100} #dict

#%%

Stu_profile1={"name":"louis","stu_id":"A123456","Score":[100,98,98,87,95]}


stu=Stu_profile1["stu_id"]
print(stu)

stu_score=Stu_profile1["Score"]
print(stu_score)

Stu_profile1["stu_id"]="B456789"

print(Stu_profile1["stu_id"])

print(Stu_profile1)


Stu_profile1["Tel"]="0912333666"

print(Stu_profile1)


del Stu_profile1["Tel"]

print(Stu_profile1)




#%%


Stu_profile2={"name":"louis","stu_id":"A123456","Score":{100,98,98,87,95}}

print(len(Stu_profile2))


Stu_profile3={"name":"louis","stu_id":"A123456","Score":{95,98,98,87,95}}

Stu_profile4={"name":"louis","stu_id":"A123456","Score":{100,96,98,87,95}}

print(Stu_profile2==Stu_profile3)

print(Stu_profile2==Stu_profile4)

print(Stu_profile2!=Stu_profile3)


print("address" in Stu_profile2)

print("address" not in Stu_profile2)

print("name" in Stu_profile2)


print(Stu_profile2.keys())

#%%

keyvalue={"X":123,"B":456,"Z":789}

print(keyvalue)

print(keyvalue.keys())

print(keyvalue.values())

print(keyvalue.items())


apple=keyvalue.fromkeys(["X","Z"],"369")

print(keyvalue)  #原始值不會變動

print(apple)


#%%


#%%

Stu_profile3={"name":"louis",
              "stu_id":"A123456",
              "Score":{"chi":89,"Eng":75,"math":88,"soci":89,"natu":89}}

stu=Stu_profile3["stu_id"]
print(stu)

stu_score=Stu_profile3["Score"]
print(stu_score)

Stu_profile3["stu_id"]="B456789"

print(Stu_profile3["stu_id"])

print(Stu_profile3)


Stu_profile3["Tel"]="0912333666"

print(Stu_profile3)


del Stu_profile3["Tel"]

print(Stu_profile3)


#***************************************

print("************************************")

print("Chi score = ",Stu_profile3["Score"]['chi'])
print("Eng score = ",Stu_profile3["Score"]['Eng'])
print("Math score = ",Stu_profile3["Score"]['math'])
print("Soci score = ",Stu_profile3["Score"]['soci'])
print("Natu score = ",Stu_profile3["Score"]['natu'])








