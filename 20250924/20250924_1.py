# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:24:53 2024

@author: USER
"""
#%%
x=10
def func():
    print(x)



func()


     




#%%

x=10

def func():
    x=200
    print("in func",x)
    print("in func",x)
    print("in func",x)

func()

print("outer func",x)

x=x+5

print("after x+5 :",x)



#%%

x=5

def f1():
    x=1
    print(x)


f1()

print(x)

#%%

x=10

def outer():
    # x=5
    y=20
    
    def inner():
        z=30
        print('x=',x)  #10
        print('y=',y)  #20
        print('inner z=',z)  #30
    inner()
    
    print('x=',x)
    print('y=',y)
    # print('outer z=',z)  
    
    
outer()

print('x=',x)
# print('y=',y)
# print('z=',z)






#%% create list (1)

list1=list()  # 等同於 list1=[]

print(list1)

print(type(list1))

list2=[1,2,3.5,4,5,"LOUIS"]

print(list2)

print(len(list2))


#%%

data=range(10)
print(data)
print(type(data))


list_x=[range(10)] # list裡面放入了range物件
print(list_x)


list_y=list(range(1,101,2))#轉型成list
print(list_y)



#%%  create list (2)

list2=list([1,2,3,4,5])   # 等同於 list1=[1,2,3,4,5]
print(list2)
print(type(list2))

#%% create list (3)

apple_list=[1,2,3,4,5,5.6,8.2,"apple"]
print(apple_list)
print(type(apple_list))


#%%
# score=[]
# name=[]

score=[85,88,95,86,84]
name=['chi','Eng','Math','Natural','Soc']


#%%
    # list(1,2,3,4,5,6,7,8,9)
listb=list(range(1,10))
print(listb)

lista=list(range(1,10,2))
print(lista)

print(type(lista))


#%%  

# list2=list([1,2.354,"louis",4.245,5])  #　等同於　list2=[1,2.354,"louis",4.245,5]
list2=[1,2.354,"louis",4.245,5]
print(list2)
print(type(list2))

#%%  

stu_data=["louis","男",28,95,85,95,78,98]
print(stu_data)
print(type(stu_data))


#%%

range_num=range(1,10) #(1,2,3,4,5,6,7,8,9)
print(range_num)
print(type(range_num))


a1_list=list(range(1,10)) #(1,2,3,4,5,6,7,8,9)
print(a1_list)
print(type(a1_list))







#%%
x=10
y="lccnet"

print(x)
print(y)


print(type(x))
print(type(y))

z=[1,2,3]
print(z)
print(type(z))


#%%


for i in range(10):  #(0,1,2,3,4,5,6,7,8,9)
    print(i)


    
for j in a1_list:  #(1,2,3,4,5,6,7,8,9)
    print(j)


#%%


lista=[range(1,10)]  # 還是range物件，不是直接看到0-9的資料
print(lista)


listb=list(range(1,10))   # 可運作，透過轉成list格式把range的資料存放進listb裡
print(listb)

# for j in range(1,10):
#     print(j)

listc=[j for j in range(1,10)]  # 可運作 透過for in 的方式一筆一筆把range的資料取出並放進listc存放
print(listc)


listd1=list(range(1,10,2))  # 可運作，透過轉成list格式把range的資料存放進listd1裡
print(listd1)


listd2=[j for j in range(1,10,2)]  # 可運作 透過for in 的方式一筆一筆把range的資料取出並放進listd2存放
print(listd2)


#C × 9/5 + 32
liste=[j*9/5+32 for j in range(2,254)]  # # 可運作 透過for in 的方式一筆一筆把range的資料取出, 且在每次抓資料出來時，運算後再存進liste裡
print(liste)


#%%

list0=[]
print(type(list0))


list1=[1,2+0j,"three",4.01,2,4,5,3,6,7,8,9,10,"apple"]

list1[3]=55   #[index]   -->index 的值是從0開始編號  ，編號0對應的就是第1個元素，編號5對應的就是第6個元素

print(list1)


list1[2]="apple"

print(list1)

list1[2]=100.256

print(list1)

list1[-2]="louis"  #[index]   -->index 的值負值的話，用倒數的方式 ，來看回來

print(list1)

print(list1[5])



#%%

a=[2,3,4,[5,6]]

b=[2,4,3.5,"Hello","apple",7]

c=[]

d=[2,[a,b]]

e=a+b

print(e)

x=a[1]

print(x)

y=b[1:3]  #1-3 (不包含3) b[1] , b[2]
print(y)


y1=b[1:]  #1-5 (不包含6) b[1] , b[2] , b[3] , b[4], b[5] 
print(y1)


y2=b[:6]  #0-5 (不包含6)  b[0] ,b[1] , b[2] , b[3] , b[4], b[5] 
print(y2)

y3=b[2:]  #2-結尾 
print(y3)

y4=b[:]  #從頭取到尾
print(y4)


#%%

print(d)

z=d[1][0][3]
print(z)


z1=d[1][0][1]
print(z1)


z2=d[1][1][-2]
print(z2)


b[0]=42
print(b)


z1=d[1][0][3][1]
print(z1)

z2=d[1][0][3][:]
print(z2)

#%%

lista=[1,2,3]
listb=[4,5,6]

listc=lista+listb
print(listc)


listd=['A,B,C']

listf=lista+listd

print(listf)


listd1=['A','B','C']

listf1=lista+listd1

print(listf1)


#%%

x_list=5*[3,2,1]

print(x_list)

y_list=3*['x','y','z']

print(y_list)

print(len(y_list))

#%%

lista=[1,3.5,'x']

listb=['x',1,3.5]

listc=[1,3.5,'x']

print(lista==listb)

print(lista==listc)

#%%

lista=[1,2,'B','C']

print('b' in lista)

print('B' in lista)

print('A' not in lista)



#%%
L=[5,10,15,20,25,30,35,40,45,50]

print(L[3])  # 20

print(L[-3])  # 40

x=L[1:5]  # 10 15 20 25

print(x)
print(type(x))

y=L[2:-2] # 不包含45
print(y)

#%%
# lista=list(range(1,10,2))

lista1=list(range(1,10,2))
print(lista1)



lista=[i for i in range(8)]  # 0....7

print(lista)


listb=[i+2 for i in range(8)] # 0....7
print(listb)


listc=[i*2+5 for i in range(8)]  # 0....7
print(listc)


#%%
# 請問 我要計算攝氏溫度0-60  --> 華氏多少度 把結果存在一個list

# 方法一

listF1=[]

for c in range(0,61):  #0->60
    print("攝氏溫度 = ",c)
    print("換算成華氏為 = ",c*9/5+32)
    F=c*9/5+32
    listF1.append(F)
    # print("執行第",c,"次","容器裡的內容",listF1)

print(listF1)


# 方法二
listF2=[c*9/5+32 for c in range(61)]  # 0....7
print(listF2)


#%%

L=[-1,1.5,66,333,333,1234]

del L[2]

print(L)

del L[2:4]

print(L)

#%%
lista=[1,3,5,7,9,10,20,30]

print(len(lista))

print(max(lista))

print(min(lista))

print(sum(lista))

lista1=[1,3.65,50.32,72.3,9,10,20,30]

print(max(lista1))

print(min(lista1))

print(sum(lista1))

lista2=[1,3.65,50.32,72.3,9,10,20,30,"lccnet"]

print(max(lista2))

print(min(lista2))

print(sum(lista2))


lista3=["apple","louis","lccnet"]

print(max(lista3))

print(min(lista3))

# print(sum(lista3))

#%%

num=[3,4,5,6,0,6,7,0,4,0,2,5]

print(num)

print(len(num))


num.append(7)

print(num)

print(len(num))

num.append(8)

print(num)
print(len(num))



print(num[1])

num[2]=0

print(num)



#%%

num.remove(6)

print(num)

del num[0]

print(num)

num.append("apple")

print(num)


#%%  # 20250925 add

num=[3,4,5,6,0,6,7,0,[4,0,2],5,0,2,5,0,0]

x=num.count(0)

for i in range(x):
    num.remove(0)

print(num)




#%%

a=[2,4,1,3,5]

b=sorted(a)

print(a)

print(b)

#%%

a1=[2,4,1,3,5]

a1.sort()

print(a1)

#%%

a2=[2,4,1,3,5,8,2.5]

a2.sort()

print(a2)


#%%

a3=[2,4,1,3,5,8,2.5,'apple']

a3.sort()

print(a3)


#%%

a4=["abc","ddd","dcc","bbb","dbc","您好嗎","12345"]

a4.sort()

print(a4)


#%%  

# ord   ord() function returns the Unicode code of a given single character
# chr   chr() function returns the character that represents the specified unicode


print(ord("a"))
print(ord("b"))
print(ord("d"))
print(ord("您"))
print(ord("1"))