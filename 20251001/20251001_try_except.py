# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:29:30 2025

@author: USER
"""

X=6

# Z=X-Y

# 10 * (1/0)

# while True print('Hello world')

print("yayaya")

'2' + 2

#%%

## input wrong datatype cause error occur

while True:
    x = int(input("Please enter a number: "))

print("Oops!  That was no valid number.  Try again...")

print("yayaya")

#%%



# # input wrong datatype cause error occur , but use try excpet to handle
while True:
    try:
        # z=x+ooo
        x = int(input("Please enter a number: "))
        break
    
    
    
    except ValueError:
        print("Oops!  That was no valid number , input integer.  Try again...")
    
    except:
        print("An exception occurred")
        break
  

print("yayaya")


#%%


try:
  print(q)
  
except:
  print("An exception occurred")
  
  
print("yayaya")

#%%
q=5
try:
  print(q)
  x = int(input("Please enter a number: "))
  
except NameError:
  print("Variable q is not defined")

except TypeError:
  print("type error")
  
# except ValueError:
#   print("ValueError")

except:
  print("Something else went wrong")
  
  
print("yayaya")

#%%
q=5
try:
  
  print("Hello")
  print(q)

#執行try 裡面的程式碼，有發生錯誤    
except:
  print("Something went wrong")


#執行try 裡面的程式碼，沒有發生錯誤  
else:
  print("Nothing went wrong")

  
print("yayaya")

#%%

try:
  # print("Hello")
  print(q)

#執行try 裡面的程式碼，有發生錯誤      
except:
  print("Something went wrong")
  
#執行try 裡面的程式碼，沒有發生錯誤  
else:
  print("Nothing went wrong") 
  
#執行try 裡面的程式碼，不管有沒有發生錯誤，都會執行以下的程式碼  
finally:
  print("The 'try except' is finished")

#%%

try:
  #f = open("test.txt",'w')
 # f = open("lccnet.txt",'a')
  f = open("apple.txt",'r')
  try:
    f.write("abc")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

print("yayaya")


#%%

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



print("yayaya")

#%%


x = 5.6

if not type(x) is int:
  raise TypeError("Only integers are allowed")
 
print("yayaya")  

#%%


def calu(x): 
    if x < 0:
      raise Exception("Sorry, no numbers below zero") 
      
try:
    calu(x = int(input("Please enter a number: ")))
  
except :
    print("error occur")
 
    
 
print("yayaya")
  


#%%


def calu(x): 
    if x < 0:
      raise Exception("Sorry, no numbers below zero") 
      
try:
    calu(x = int(input("Please enter a number: ")))
  
except Exception as abc:
    print("qqq : ", abc)
    print("error occur")
 
print("yayaya")

#%%
  # ref  :　https://docs.python.org/zh-tw/3.13/tutorial/errors.html#exceptions






