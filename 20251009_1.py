# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 09:34:45 2025

@author: USER
"""

x = 5

def myfunc():
  # global x
  x=10
  print(x)
  x = x + 10
  print(x)
  
myfunc()

print("Python is " , x)

#%%


y="lccnet"

def myfunc():
    global y
    y=y+" is good"

myfunc()

print("Python is " + y)
