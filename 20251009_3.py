# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:45:45 2025

@author: USER
"""
"""
    Arbitrary Arguments, *args
    If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

    This way the function will receive a tuple of arguments, and can access the items accordingly:
"""


def my_function(x,*kids):
  for y in kids:
  	print(y)
  #print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus","lccnet","apple")


#%%

"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:


"""

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#%%
"""
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
"""

def my_function(x, /):
  print(x)

my_function(3)

# #error
# def my_function(x, /):
#   print(x)

# my_function(x = 3)

#%%

"""
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:

"""
def my_function(*, x):
  print(x)

my_function(x = 3)


# #error
# def my_function(*, x):
#   print(x)

# my_function(3)

#%%


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


