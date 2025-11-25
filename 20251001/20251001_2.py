# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:50:28 2023

@author: OfficePC
"""
#%%

import numpy as np

data=[[1,2,3],[4,5,65],[7,5,10],[7,5,10],[7,5,10]]

arr=np.array(data)

dim_value=arr.ndim

print(dim_value)

shape_value=arr.shape
print(shape_value)

dtype_value=arr.dtype

print(dtype_value)



itemsize_value=arr.itemsize

print(itemsize_value)



nbytes_value=arr.nbytes

print(nbytes_value)



#%%

import numpy as np
x=np.random.randn(5,4)

print(type(x))

print(x)

print(x.mean())

print(x.sum())

print(x.max())

print(x.min())

data=np.array([[1,2,3],[4,5,65],[7,5,10],[7,5,10],[7,5,10]])

print(data.cumsum())

print(np.std(data))

#%%

import numpy as np
# x=np.random.rand(5,4)*100
# print(x)

y=np.random.randint(0,100)
print(y)

#%%

import numpy as np
x = np.arange(12)
print(x)

print("************************")
x2d = np.arange(12).reshape(3,4)
print(x2d)

print("************************")
y2d = np.arange(12).reshape(12,1)
print(y2d)

z2d = np.arange(12).reshape(1,-1)
print(z2d)


a=x2d[1][1:];print(a)

# equal
print("************************")

b=x2d[1][1:]
print(b)

a[0]=-1

print(x2d)
print(a)
print(b)

#%%
a=[1,2,3,4,5]
b=a

b[3]=100
print(a)

#%%
x=100
y=x

print(y)

y=200

print(x)
print(y)

#%%

x = np.arange(12).reshape(3,4)
print(x)

y=x[[0,1,2],[2,1,0]]
print(y)

print(x[np.ix_([0,2],[1,3])])

print(x[np.ix_([0,1],[0,2])])

#%%
import numpy as np
arr=np.arange(10)

print(arr)

x_slice=arr[5:8]
print(x_slice)

arr[5:8]=7

print(x_slice)
print(arr)

#%%

import numpy as np
a=np.array([1,2,3])
b=np.array([2,2,2])

z=a*b
print(z)

c=np.array([3.0,2.0,1.0])
d=5
k=c*d
print(k)

#%%


import numpy as np
a=np.arange(6)
print(a)
b=a.reshape(6,1)
print(b)

c=np.ones(5)
print(c)

d=b+c

print(d)


#%%

import numpy as np
a=np.array([1,2,3])

#%%

import pandas as pd

x_series=pd.Series([4,7,-5,3.])

print(x_series)

print(type(x_series))

#%%

import pandas as pd

x_series=pd.Series([3,6,-9,12])

series_value=x_series.values

print(series_value)

index_value=x_series.index

print(index_value)

x_series_value=x_series[1]

print(x_series_value)

#%%

import pandas as pd

x_series=pd.Series([3,6,-9,12],index=['a','b','c','d'])

series_value=x_series.values

print(series_value)

index_value=x_series.index

print(index_value)

x_series_value=x_series['b']

print(x_series_value)

print('a' in x_series )

print('e' in x_series )

#%%

import pandas as pd

data={'name':['Bob','Nancy','Eric'],'year':[2023,2024,2022],'month':[1,2,7],'day':[15,20,1]}

print(type(data))

print(data)

print('******transform to dataframe******')

myframe=pd.DataFrame(data)

print(type(myframe))

print(myframe)



#%%

import pandas as pd

data={'name':[0],'year':[0],'month':[0],'day':[0]}

print(type(data))

print(data)

print('******transform to dataframe******')

myframe=pd.DataFrame(data)

print(type(myframe))

print(myframe)


#%%

import pandas as pd

data={'name':['Bob','Nancy','Eric'],'year':[2023,2024,2022],'month':[1,2,7],'day':[15,20,1]}

print(type(data))

print(data)

print('******transform to dataframe******')

myframe=pd.DataFrame(data)

print(type(myframe))

print(myframe)

myframe1=pd.DataFrame(data,columns=['name','year','day','month'])

print(type(myframe1))

print(myframe1)

#%%

df=pd.read_csv('csv_output.csv',encoding='big5')

print(df.head(1))
print("**********************")
print(df.tail(1))