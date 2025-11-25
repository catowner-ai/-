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

print(q)
  
print("yayaya")
#%%


try:
  print(q)
  
except:
  print("An exception occurred")
  
  
print("yayaya")

#%%
# q=5
try:
  print(q)
  x = int(input("Please enter a number: "))
  
except NameError:
  print("Variable q is not defined")

except TypeError:
  print("type error")
  
except ValueError:
  print("ValueError")

except:
  print("Something else went wrong")
  
  
print("yayaya")

#%%
q=5
try:
  
  print("Hello")
  print(q1)

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
  # f = open("test.txt",'w')
  f = open("lccnet.txt",'a')
  # f = open("apple.txt",'r')
  try:
    f.write("apple")
  except:
    print("Something went wrong when writing to the file")
  
  finally:
    print("finally")
    f.close()
except:
  print("Something went wrong when opening the file")

print("yayaya")


#%%

x = -1
try:
    if x < 0:
      print("lccnet")
      raise Exception("Sorry, no numbers below zero")
except:
    print("input number")


print("yayaya")

#%%  輸入浮點數，會發生TypeError，程式就停了
x = 5.35

if not type(x) is int:
  raise TypeError("Only integers are allowed")

print("yayaya")  

#%% 　　 
#輸入浮點數，會發生TypeError，因為有寫try excpet，
#所以程式有處理，就可以繼續往下執行程式

x = 5.35
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
        
except TypeError:
    print("Only integers") 
    
print("yayaya")  

#%%


def calu(x): 
    if x < 0:
      raise ValueError("Sorry, no numbers below zero") 
      
try:
    calu(x = int(input("Please enter a number: ")))

    
except ValueError:
    print("ValueError") 
except :
    print("error occur")
 
    
 
print("yayaya")
  


#%%


def calu(x): 
    if x < 0:
      raise Exception("Sorry, no numbers below zero") 
      
try:
    calu(x = int(input("Please enter a number: ")))
  
except Exception as memo:
    print("error message : ", memo)
    print("error occur")
 
print("yayaya")

#%%
  # ref  :　https://docs.python.org/zh-tw/3.13/tutorial/errors.html#exceptions






