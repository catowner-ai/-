# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:24:38 2023

@author: USER
"""
         #0          #1           #2
list_x=[[1,2,3],[4.0,5.2,65.2],[7,5,10]]
print(list_x)
print(type(list_x))

print(list_x[2][1])


print("***********************************")

import numpy as np    #numpy的簡稱np   #二維轉np

numpy_x=np.array([[1,2,3],[4.0,5.2,65.2],[7,5,10]])
print(numpy_x)
print(type(numpy_x))

#%%
                           #不管是什麼資料,可以直接轉換
import numpy as np         #跟上面資料不一樣是()裡面資料是數組
numpy_y=np.array(((1,2,3),(4.0,5.2,65.2),(7,5,10))) 
print(numpy_y)
print(type(numpy_y))

#%%   #後面不太會用到
import numpy as np             #只要數字裡面有整數或浮點數，都會統一轉換成浮點數

x=np.array([1,2,3],dtype=complex)   # dtype=complex 轉換過程中順便指定
print(x)
print(type(x))


y=np.array([1,2,3],dtype=float)   #dtype=float 指定轉換成浮點數
print(y)
print(type(y))

#%%


import numpy as np                        
x_list=[[1,2,3],[4.0,5.2,65.2],[7,5,10]]

x_numpy=np.array(x_list,dtype=float)
print(x_numpy)
print(type(x_numpy))


y_numpy=np.array(x_list,dtype=complex)
print(y_numpy)
print(type(y_numpy))

#%%

import numpy as np      #載入np套件

x_zeros=np.zeros((3,5)) #np.zeros 裡面數字為0 #呈現3列5欄 行列式都是2維資料
print(x_zeros)
print(type(x_zeros))



y_arange=np.arange(3,21,2,dtype=float)  #每次間隔2,資料預設浮點數,arange尾數不包含
print(y_arange)
print(type(y_arange))



print('****************************')
z_arange=np.arange(3,21,2)
print(z_arange)
print(type(z_arange))


x_ones=np.ones((3,5))  #np.ones裡面數字為1,預設浮點數
print(x_ones)
print(type(x_ones))



x_arange_float=np.arange(0.01,0.04,0.01)
print(x_arange_float)

#%%


import numpy as np

data=[[[1,2,3],[4.0,5.2,65.2],[7,5,10],[7,5,10]]]   #二維資料list

arr=np.array(data)            #arr資料型態float64

dim_value=arr.ndim

print(dim_value)

shape_value=arr.shape
print(shape_value)             #總共4筆資料,每筆資料裡面三個數字
                               #只要數字裡面有整數或浮點數，都會統一轉換成浮點數
dtype_value=arr.dtype
                 
print(dtype_value)             #查看資料型態
                        


#%%


import numpy as np

data=[[1,2,3],[4,5,65],[7,5,10],[7,5,10]]

arr=np.array(data)

dim_value=arr.ndim

print(dim_value)

shape_value=arr.shape
print(shape_value)

dtype_value=arr.dtype

print(dtype_value)      #跟上面例子一樣,只是裡面沒有浮點數,所以統一都是整數


#%%

arr_int32 = arr.astype(np.int32)       #改變程式格式型態 從int64改為int32

arr_int32_dtype_value=arr_int32.dtype

print(arr_int32_dtype_value)

print(arr_int32)

#%%


lista = [1,2,3]
listb=[[1,2],[3,4]]

