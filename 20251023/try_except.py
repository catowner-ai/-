# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:29:30 2025

@author: USER
"""

# try測試程式碼在執行中是否有錯誤。(如果有錯誤會產生出例外物件)
# except 用此語法捕捉例外物件並做適當的處理。
# else 當在「沒有」錯誤時執行要執行的程式區塊。
# finally 不管是否有發生例外事件，都會執行此區塊的程式碼。

# apple=5

print(apple)

print("No variable so An exception occurred")

print("lccnet")


#%%

# example 1
#apple=5

try:   
  print(apple)
  
  
except:
  print("No variable so An exception occurred")
  
  
print("ok")
print("lccnet")

#%%

# example 2

try:
  print(123445)
  print("lccnet")
  # print(apple)
  x = int(input("Please enter a number: "))  
  print("ok")

except NameError: # 有指定except類型。
  print("apple variable  is not defined")

except ValueError: # 有指定except類型。
  print("請輸入整數")
  
except: # 未指定except類型。
  print("未指定except類型的錯誤")
  
print("yayaya")
  
#%%

#example 3  
try:
  print(iphone17)
  # print("This is try except test")
 
#執行try裡面的程式有發生錯誤，就會執行這範圍的程式  
except:
  print("An excpet occurred")
  
 #執行try裡面的程式「沒有」發生錯誤，就會執行這範圍的程式   
else:
  print("no excpet occurred")

    
#不管有無發生錯誤，程式都繼續往下走
print("88888")


#%%

#example 4  

try:
    print(apple)
  # print("This is try except test")
    
  
except:
  print("apple variable  is not defined")
  
#執行收尾動作  
finally:
  print("不管是否有發生例外事件，都會執行此區塊的程式碼")




#%%

#%%
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
  print(P)

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
  # f = open("lccnet.txt",'a')
  f = open("apple.txt",'r')
  try:
    f.write("abc")
  except:
    print("Something went wrong when writing to the file")
  else:
    print("nothing")
  finally:
    f.close()
        
except:
  print("Something went wrong when opening the file")

print("yayaya")


#%%

x = -1

try:
    if x < 0:
      raise Exception("Sorry, no numbers below zero")
      
except:
    print("numbers below zero")


print("yayaya")

#%%

x = 5

try:   
    if not type(x) is int:
      raise TypeError("Only integers are allowed")
      
except TypeError:
    print("type is wrong")
 
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






