# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:47:19 2025

@author: USER
"""

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


#%%

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    
#%%
    
day = 9

match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    
  case _:
    print("NO Match")  
    
#%%
    
    
    
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month > 2:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month >5:
    print("A weekday in May")
  case _:
    print("No match")