# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:08:28 2024

@author: USER
"""
#浮點數

print(3.14)  #印出浮點數

print(type(3.14))  #印出其3.14的資料型態

print(3.14e5)    # 3.14乘以10的5次方

print(3.14e-5)   # 3.14除以10的5次方

print(float('125.361'))  #把'125.361'的數「字」。轉成浮點數

# print(int('125.361'))   #把'125.361'的數「字」。轉成整數(會錯誤，也就是不能這樣做)

print(int('1334'))       #把'1334'的數「字」。轉成整數

print(int(13.254))       #把13.254的浮點數。轉成整數







#%%



print(type(10))

print(type(2.5))

print(type('abcde'))

print(float('1.234'))

print(int(3.14))

#%%

print(type('1.234'))

# print('1.234'+56478) # '1.234'數「字」無法跟數值做運算  (會錯誤，也就是不能這樣做)

print(float('1.234')+56478)

#%%

print(5<3)

print(5>3)

print(5*10>=50)

print(bool(123456))

print(bool(0))

#%%

print('lccnet')

print("lccnet")

print("""1
      2
      3""")


#%%




# 12  36
print('c:\todo')  # \t 就等同於按下鍵盤的tab按鍵
  #    c: odo


print('c:\\todo')  # \t 就變成單純的文字，無任何功能
  #    c:\todo


print('\\t')
print(r'\tapple\tlccnet\n')  #以上這二種功能一樣


# 打四個斜線會有兩個斜線不見  

print("\\\\ttt")

#%%

print(r'c:\nodo\louis\apple\sony')

print('c:\\nodo\\louis\\apple\\sony')



#%%

# %s指的是輸出字串

# %d指的是輸出整數內容

# %f指的是輸出浮點數的內容

print('%s哈囉!     !'  %'世界')

print('你目前的存款為 %.8f元'  %10000)

print('被除數 : %d 除以 %d 為 %f' %(10,3,10/3))

print('被除數 : %05d 除以 %05d 為 %.2f' %(10,3,10/3))

print('被除數 : %-5d 除以 %-5d 為 %.2f' %(10,3,10/3))

print('被除數 : %-5d 除以 %-5d 為 %10.2f' %(10,3,10/3))



#%%
x=314000000000000000

print('您目前的存款只剩 %e , %d 元' %(x,100) )

print('您目前的存款只剩 %.3e , %d 元' %(x,100) )


#%%
a=12.4
b=2

print(type(a))
print(type(b))



# x=314000000000
# print('您目前的存款只剩 %e , %d 元' %(x,100) )
print('a+b = {:.2f} ,a-b = {:f}'.format(a+b,a-b))

print('a+b = {:.2f}'.format(a+b))

print('b-a = {:.2f}'.format(b-a))

print('value is  {:.0f}'.format(2.618)) #四捨五入

print('value is  {:0<7d}'.format(51)) 

print('value is  {:x<4d}'.format(51)) 

print('value is  {:x>4d}'.format(10)) 

print('value is  {:,}'.format(1000000)) 

print('value is  {:.0%}'.format(0.25)) 




#%%
a=12.4
b=2

print('a-b = {1:.2f} ,a+b = {0:f} ,a*b = {2:f}'.format(a+b,a-b,a*b))
                                                 #      0   1   2  的位置  --> 

#%%

a=1
b=2
c=3.6
d=3.6

print(int(a+c),int(a+d))  # 成本考量


print(a+c,a+d)            # 數據精準度考量


#%%
#bit  -->
#8bit --> 1byte 
#1024byte  --> 1Kbytes  
#1024Kbyte --> 1Mbytes  
#1024Mbyte --> 1Gbytes  
#1024Gbyte --> 1Tbytes


#%%
print(float(a+b))

#%%
print(int('10'))
print(int(3.145))
#print(int('3.145')) #(x)
print(int(True))
print(int(False))


#%%

#二進制
print(0b1010)  # 0b  -->binary(2進制)
#   11
#   01+
# -----
#  100

#十進制
print(10)  # 0-->9, 10
#     09
#     01+
#   -----
#     10  

#十六進制
print(0xa)    # 0x  -->16進制
# 0 1 2 3 4 5 6 7 8 9 a b c d e f (每一個位數可儲存的數值)

#   0f
#   01+
# ----- 
#   10

print(0b111110)

#%%

StuName="louis"

# StuName=15

# StuName=152.021


print('%s學員名稱為 ' % StuName)

print('學員名稱為 = ',StuName)

TeaName='louis'
print('老師名稱為 %s' % TeaName)


StuName=10000
print('薪水為 %d' % StuName)

StuName=325.0241
print('薪水為 %f' % StuName)

#%%

##　java 宣告變數 ##

# String StuName ;
# StuName='louis' ;

# StuName=10000; (X)

##　java 宣告變數 ##

#%%

a=12.4
b=2
c=3
d=3.6

print("a的值為:",a,"是否是...","b的值為",b)

print("b的值為:",b)

print("c的值為:",c)

print("(a+b) = %.2f " % (a+b))

#%%
eleven1=500
print(eleven1)
a=1
b=3
c=5

print(a)

del a

# print(a)


#%%

a=1
print(type(a))

a='abc'
print(type(a))

a=123.456
print(type(a))



#%%
a=12.4110
b=2
print(float(a+b))

print(round((a+b),2))

#%%

print(10//3)

print(7+8)

print(26%8)

print(17.675%5)


print(2.675==2.675)

print(2.675==17.675%5)

print(2.675==(17.675%5))

x1=float(7+8.123)
print(x1)

x2=7+8.123
print(x2)

y=float(17.675%5)



x=17.675%5
print(x)

print(round((x),4))



print(7/2)

print(7//2)

print(9**0.5)

print(9**2)

print(9-2)

print(9*2)




#%%


print(123=='123')

print('ABC'=='abc')

print(True==1)

print(False==0)


#%%

pow(9,1/2)



#%%
a=12.40
b=2.0

c=12.4000
d=2.0


z=b+d
q=4

print(a>b)

print(a<b)

print(a==c)

print(b==d)  
 
print(z==q)

print(z!=q)

#%%

print('a+b = {0:.2f} , a-b={1:.5f} , abcde={2:s}'.format(a+b,a-b,"您好"))

print('a-b = {1:.5f} , a+b={0:.2f} '.format(a+b,a-b))



#%%
print(2>1)
print(2>1==False)
print(2>1==True)

a=1
b=2
c=3
d=4

z=a+b*c-d
print(z)

q=(a+b)*c-d
print(q)

#%%
a=10
b=20
a=b
print(a)


#%%
a=10
b=20

a+=b   # a=a+b

print(a)

#%%
a=10
b=20

a-=b   # a=a-b

print(a)

#%%
a=10
b=20

a*=b   # a=a*b

print(a)

#%%
a=10
b=20

a/=b   # a=a/b

print(a)

#%%
a=10
b=20

a//=b   # a=a//b

print(a)

#%%
a=10
b=20

a%=b   # a=a%b

print(a)


#%%
a=10
b=5

a**=b   # a=a**b

print(a)



#%%
a=10
b=5
c=7
d=3
z=20

   # a=a*b

a*=b+c-d+200-z

# -->a=a*b+c-d+200-z  (x)

# -->a=a*(b+c-d+200-z) (o)

print(a)


#%%
#%%
a=10
b=5
c=7
d=3
z=20

a*=b+c-d+200-z

#(1) a=a*b+c-d+200-z
#(2) a=a*(b+c-d+200-z)

# -->a=a*b+c-d+200-z  (x)

# -->a=a*(b+c-d+200-z) (o)

print(a)


#%%

x,y,z=10,20,30

# x=10
# y=20
# z=30

x*=y

z%=5





#%% and (二個要同時成立就成立)
#    False    True
print(1>4 and 3>2)
#    True    True
print(4>1 and 3>2)

#%% or (有一個成立就成立)
#    False    True
print(1>4 or 3>2)

#    True    True
print(4>1 or 3>2)

#    True    False
print(3>2 or 1>4)

#%% not (輸出結果作反向)

#       False    
print(not 1>4)  #True

#         True    
print(not 4>1)  #False


#%%

name='apple'

print('Hello',name,'Nice','to','meet you')

print()

#%%

name='lccnet'

print('Hello',name,'Nice','to','meet you',end='!!!!!')

#%%

name='lccnet'

print('Hello',name,'Nice','to','meet you',sep='____')


#%%

userName=input('請輸入姓名')
print("您的姓名 : ",userName)

#%%
PI=3.1415926
radius=input("請輸入圓半徑:")
print(type(radius))  # string  不能數學運算

#%%

PI=3.1415926
radius=eval(input("請輸入圓半徑:"))  # 用eval把輸入的數「字」轉換成數(值)
print(type(radius))  # int or float  可以數學運算
print("半徑為", radius, "的圓面積為", PI * radius * radius)


#%%


PI=3.1415926
radius=int(input("請輸入圓半徑:"))  # 用int強迫轉型成整數
print(type(radius))  # int 可以數學運算
print("半徑為", radius, "的圓面積為", PI * radius * radius)


#%%

PI=3.1415926
radius=float(input("請輸入圓半徑:")) # 用float強迫轉型成浮點數
print(type(radius))  # float  可以數學運算
print("半徑為", radius, "的圓面積為", PI * radius * radius)





