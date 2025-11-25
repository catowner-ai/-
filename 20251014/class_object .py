# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:17:19 2023

@author: USER
"""

class Dog:
    x=10
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)



class Cat:
    y=5
               # mistaken use of a class variable
    def __init__(self, name):
        self.name = name

    def sound(self, sound_type):
        print("叫聲 : = ",sound_type)
              
    
d = Dog('Lccnet')
# -->　＿＿init__
#--> d.name=Lccnet

print(d.name)

e = Dog('Iphone17')
# -->　＿＿init__
#--> e.name=Iphone17



catf =Cat("louis")
# -->　＿＿init__
#--> catf.name=louis


catf.sound("Mew")



catapple =Cat("apple")
# -->　＿＿init__
#--> catapple.name=apple
catapple.sound("ju")



#%%

print(catf.name) # louis

print(catapple.name) # apple

print(d.name)

print(e.name)



d.add_trick('123456')
e.add_trick('abcdefg')



#%%
print(d.tricks)
print(e.tricks)

print(d.x)
print(e.x)

d.x=200
print(d.x)
print(e.x)


#%%

d.tricks=[123]

print(d.tricks)
print(e.tricks)

#%%

e.tricks.append(456)

print(d.tricks)
print(e.tricks)

