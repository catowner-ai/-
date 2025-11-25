# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:57:29 2024

@author: USER
"""
#%%

print("請輸入二個整數數字")

m=int(input("請輸入第一個整數數字 : ")) # 3
n=int(input("請輸入第二個整數數字 : ")) # 10


while n!=0: # (1) True  (2) True (3)True  
    r=m%n   # (1) r=3   (2) r=1  (3)r=0
    m=n     # (1) m=10  (2) m=3  (3)m=1
    n=r     # (1) n=3   (2) n=1  (3)n=0 
    if m==1:
        print("互質")
        break  # 會跳離整個while迴圈的整個控制 -->跳到24行後
else:
    print("最大公因數 : ",m)
    
    
    
print("while done ")



#%%

answer = input(" 請輸入「快樂」的英文： ")
while answer.upper() != "HAPPY":    
    answer = input(" 答錯了， 請重新輸入「快樂」的英文： , 輸入exit就不要再猜了")
    if answer.upper()=="EXIT":
        print("我猜不到，我不玩了，我要離開")
        break

print("程式已結束")    


#%%

# range(10)  # 0,1,2,3,4,5,6,7,8,9  (不包含括號內的數字，數字範圍從0開始)

# range(8)  # 0,1,2,3,4,5,6,7  (不包含括號內的數字，數字範圍從0開始)

# range(5)  # 0,1,2,3,4  (不包含括號內的數字，數字範圍從0開始)



# list --> python的容器  -->串列

a=list(range(10))  # 0,1,2,3,4,5,6,7,8,9  (不包含括號內的數字，數字範圍從0開始) , 把range的內容轉成list放進a來存放
print(type(a))
print(a)



a1=list(range(7))  # 0,1,2,3,4,5,6
print(a1)


b1=list(range(1,10,2)) #1,3,5,7,9
print(b1)


c1=list(range(10  ,  -10 ,  -2)) #10,8,6,4,2,0,-2,-4,-6,-8   不包含結尾的數字
             #開頭    結尾   間隔 
             
print(c1)


c2=list(range(0 ,  1000 ,  3)) # 0-1000每次間隔3 ，不包含1000
             #開頭    結尾   間隔 

#%%

for w in range(5):  # 0,1,2,3,4
    print(w)      #(第1輪) 0  (第2輪) 1  (第3輪) 2  (第4輪) 3  (第5輪) 4




#%%

c1=list(range(10  ,  -10 ,  -2)) #10,8,6,4,2,0,-2,-4,-6,-8   不包含結尾的數字
             #開頭    結尾   間隔 
             
for w in c1:  #10,8,6,4,2,0,-2,-4,-6,-8   不包含結尾的數字
    print(w+5)



#%%
      #0,1,2,3,4 .... 99

for i in range(100):
    print("test")
    print(i)


#%%

x=5
y=10
z=15

result=x+y*z   # x+y-z   



#%% 
z=0

for i in range(0,101,2):  #(0,1,2,3,4)  
# for i in (0,1,2,3,4):  #(0,1,2,3,4)
    print(i) 
    z=z+i
    
    
print("z_value is :",z)

#%%

name ='iphone'
print("name字串長度是 :",len(name))

for i in range(len(name)): # 0,1,2,3,4,5,...13
    print(i,name[i])  #[]索引編號是從0開始抓資料 ，索引[0]代表第一個元素，索引[1]代表第二個元素


#%%
x='apple'
y='iphone'

z=x+y  # appleiphone
print(z)
x=2 
y=3
#print(int("1"))  #數字1 轉成整數1

print(str(x)+"*"+str(y)+"="+str(x*y))     #整數數值1 轉成文字1
  #       2   *     3    =    6



#%%
for i in range(1,10): #0,1,2
    for j in range (1,10): #0,1,2,3
       print(str(i)+"*"+str(j)+"="+str(i*j))

#%%

# x1,x2=10,20
result1,result2='',''
for i in range(1,10): #(1) 1,2
    result1=''
    for j in range(1,10): #(1) 1,2,3,4,5,6,7,8,9
        result1=result1 + str(i) + '*' + str(j) + '=' + str(i*j)+'\t' #(1) result1='1*1=1'+'1*2=2' (2) result1='1*1=1'+'1*2=2'
                    #(1回合)1*1=1   1*2=2    1*3=3   1*4=4   1*5=5 
                    #       2*1=2    2*2=4  
    print(result1)
    result2=result2+result1+'\n'
print(result2)

#result2=result2+result1+'\n' 能改成result2+=result1+'\n' 嗎
                          #  --> result2=result2+(result1+'\n')

#%%
for i in range(24): #0,1,2
    for j in range (8): #0,1,2,3,4,5,6,7
        print("abc")


#%%

print('apple'+'iphone')

print('apple'+'\t'+'iphone')

print('asus'+'TUF')

print('asus'+'\n'+'TUF')

print('asus'+' '+'TUF')

#%%

answer = input(" 請輸入「快樂」的英文： ")
while answer.upper() != "HAPPY":
    if answer.upper() == "QUIT":
        print(" 我不玩了！ ")
        break
    answer = input(" 答錯了，請重新輸入「快樂」的英文： ")
else:
    print(" 答對了！ ")

print('Quit while')

#%%

i=0
while i<1001:
    i=i+1
    if i%9!=0:
        continue #繼續下一輪的迴圈
    print(i)
    
    
    
#%%

def CtoF1(degreeC,c2,c3):  # degreeC 是一個參數
    degreeF=degreeC*1.8+32
    print("攝氏",degreeC,'度可以轉換成華氏',degreeF,'度')
    print("c2 = ",c2)
    print("c3 = ",c3)




#%%

def CtoF2(degreeC):  # degreeC 是一個參數
    degreeF=degreeC*1.8+32
    print("攝氏",degreeC,'度可以轉換成華氏',degreeF,'度')
CtoF2(30)



#%%
    

while(115):  #布林代數 , True -->非0的數都叫True  , 0 None ,'' --> False
    temperatureC=eval(input("請輸入攝氏溫度值，輸入0即停止轉換"))
    if temperatureC == 0:
        print(" 我不玩了！ ")
        break
    CtoF1(temperatureC,c3=10,c2=20)  # temperatureC所代表的就是一個引數





# i=1
# while(i<=10):
#     temperatureC=eval(input("請輸入攝氏溫度值，輸入0即停止轉換"))
#     if temperatureC == 0:
#         print(" 我不玩了！ ")
#         break
#     CtoF1(temperatureC)
#     i+=1;




#%%

def teaTime(dessert, drink = '紅茶',cookie='布丁'):
    print('我的甜點是 ', dessert, ' 飲料是 ', drink, ' 餅乾是 ', cookie)
    
    
teaTime('馬卡龍 ', '咖啡')



teaTime('帕尼尼')

teaTime(dessert = '三明治 ', drink = ' 奶茶')

teaTime('紅豆餅 ', drink = ' 綠茶')
teaTime('紅豆餅 ',cookie="pie", drink = ' 綠茶')





# dessert=input("請輸入dessert")
# drink=input("請輸入drink")
# teaTime(dessert) #the same --> # teaTime('帕尼尼')

# print("test2")
# teaTime(dessert,drink)

#%%

def trapezoidArea(top, bottom, height):
    result = (top + bottom) * height / 2
    print('這個梯形面積為 ', result)
    
trapezoidArea(10, 20, 5)


trapezoidArea(10, height = 5, bottom = 20)


trapezoidArea(height = 5, bottom = 20, top = 10)

#%%

def divmod2 (x,y):
    div = x // y #14
    mod = x % y  #2
    print("商數是 = " ,div )
    print("餘數是 = ",mod )
    return div, mod  #14,2 # return 是要把運算結果回傳回來，供後續使用, 執行完return函式就結束了
    



# divmod2 (100,7)  #14,2

#a,b=14,2
a, b =divmod2 (100,7)  #14,2
print('100除以 7 的商數為 ', a, '，餘數為 ',b)

c, d =divmod2 (200,13)
print('200除以 13 的商數為 ', c, '，餘數為 ',d)

q =divmod2 (300,13)
print('q的值為 = ',q)

print(type(q))


#%%









    
    