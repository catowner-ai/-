# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:33:13 2024

@author: USER
"""

#%%
x=5
y=10
z=5

if 5:
    
 # pass
    print("lccnet1")

    #pass


print("lccnet")


#%%
x=15
y=10
z=5

if x>y and z>y:  
    z=x-y
    print('1_x比y大',z)
    print('2_x比y大',z)
    print('3_x比y大',z)
    print('4_x比y大',z)
    print('5_x比y大',z)
 
    
print('done')

#%%

if 2**10==1024:
    print("2^10=1024")
    print("2^10=1024")
    print("2^10=1024")
    print("2^10=1024")



#%%
x=70

score = eval(input('請輸入python 的成績:'))

print(type(score))

if score >=60:
    print("及格")
    print("及格")
    print("及格")   
else:
    print("不及格")
    print("不及格")

# print("不及格")
print('done')

#%%

x=15
y=10
z=5

print(x)
print(y)
print(z)

#%%
num = eval(input("請輸入數值"))
if num!=0:
    if num%2 ==0:
        print(num,'是偶數')
    else:
        print(num,'是奇數')
else: print('這是零重打')
 
    
 
    
#%%
score=eval(input("請輸入python成績:(0-100)"))


if score >100 or score <0:
    print("your score is not in score range")

else:
    if score >=90: 
        # print("Grade A")
        if score ==100:
            print("Grade S")
        elif score<100 and score>=95:
            print("Grade S-") 
        else:
            print("Grade A")      
    elif score <90 and score>=80:
        if score>=85:
            print("Grade B+")
        else:
            print("Grade B")
    elif score <80 and score>=70:
        print("Grade C")
    elif score <70 and score>=60:
        print("Grade D")
    else:
        print("fail")
    
#%%
score=eval(input("請輸入python成績:(0-100)"))
if score >100 or score <0:
    print("your score is not in score range")
    
else:
    if score >=90:
        print("Grade A")
    elif 90>score>=80 :
        print("Grade B")
    elif 80>score>=70:
        print("Grade C")
    elif 70>score>=60:
        print("Grade D")
    else:
        print("fail")
    
#%%
x=10
y=3
print("abc")

if (x>=10):
    print("cde")
    if y<5:
        print("y<5")
        
#%%
    
num1=int(input("input num1:"))  
num2=int(input("input num2:"))

if num1==num2:
    print("equal")
elif num1>num2:
    print("num1>num2")
else:
    print("num1<num2")
    
#%%

score=eval(input("請輸入python成績:(0-100)"))
if score >=90:
    print("Grade A")
else:
    if score>=80:
        print("Grade B")
    else:
        if score>=70:
           print("Grade C") 
        else:
            if score>=60:
                print("Grade D") 
            else:
                print("fail")
#%%
i=6

while i>5:
    print(i)
    i=1 #--> i=i+1

print("while done",i)

#%%

answer = input(" 請輸入「快樂」的英文： ")

print(type(answer))

# answer.lower()!='happy'
while answer.upper() != "HAPPY":
    answer = input(" 答錯了， 請重新輸入「快樂」的英文： ")
    
else:
    print(" 答對了！ ")
    print(" 答對了！ ")
    
print("Hello")
#%%

answer = input(" 請輸入「快樂」的英文： ")
while answer.upper() != "HAPPY":    
    answer = input(" 答錯了， 請重新輸入「快樂」的英文： ")


    
print(" 答對了！ ")
print(" 答對了！ ")


#%%

answer = input(" 請輸入「快樂」的英文： ")
while answer.upper() == "HAPPY":
    answer = input(" 答對了 , 請再次輸入")

print(" 答錯了！ ")

#%%

    
    
    
        
        