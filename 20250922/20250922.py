# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 20:32:26 2025

@author: LouisOffice
"""

    
print ("Hello, 陳之漢!\n")

print("lccnet")

#%%


print(type(10)) #查詢資料型態type 整數

print(type(2.3456))  #查詢資料型態type 浮點數

print(type("lccnet"))  #查詢資料型態type  字串


#%%

#******************************************#
# 2 進制 0>1>10>11>100
    

# 10 進制  0 > 9  > 10 11 12 13  .. 19  > 20 
# ..... 99   > 100


# 16 進制  0 > 9 (A 10) (B 11) (C 12) --> (F 15) --> 10
# 0x1f  --> 16 +15-->31



#******************************************#

# 137(10進制) >  轉2進制是 ?

# 1000 1001
# 128 +8 + 1 

# 128+9(8+1)

# 0  1  1  1 0 1 1 01       >  10進制是?
#  128+64+32 + 8+4 +1  


#%%

print(0b011101101) # -->50        二進制轉10進制輸出

print(0o62)  # 8*6+1*2  -->50     八進制轉10進制輸出

print(0x32)  # 16*3 +1*2  -->50   十六進制轉10進制輸出

print(50)   #-->50                十進制轉10進制輸出


#%%

print(type(3.14))

print(3.14e-2)  #浮點數


x=float('1.234')  # 1.234數「字」  --> 轉成 1.234數值 存給x變數

print(x)

print(type(x))

#%%

y='250.25'
z=10
q=z+float(y)
print(q)




y1='250'
y2=250.25

z1=10
q1=z1+int(y1)
print(q1)


#%%


x1=float('1')  # 1數「字」  --> 轉成 1數值 存給x變數 (浮點數)

print(x1)

print(type(x1))

#%%


x2=int('1')  # 1數「字」  --> 轉成 1數值 存給x變數 (整數)

print(x2)

print(type(x2))

#%%

# char  --> 1byte  --> 8bit --> 2的8次方
# int   --> 4byte  --> 32bit --> 2的32次方

# bit  --> 0,1
# byte --> 8bit 
# 1kbyte --> 1024byte
# 1Mbyte --> 1024kbyte
# 1Gbyte --> 1024Mbyte
# 1Tbyte --> 1024Gbyte


#64k

#%%

#%%


y=int(3.64)      # 3.64浮點數數「值」  --> 轉成3整數數值 存給y變數

print(y)

print(type(y))


#%%
z=int('3.14')      # 3.14浮點數數「字」  --> 轉成3整數數值 存給z變數

print(z)

print(type(z))


#%%

print(5>3)  #5 是否大於 3 

print(5*10>50) #5*10 是否大於 50 

print(bool(12345))

print(bool(12.35))

print(bool('lccnet'))

print(bool(0))


