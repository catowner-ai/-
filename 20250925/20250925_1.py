# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 20:21:30 2025

@author: LouisOffice
"""

thislist = ["apple", "banana", "cherry"]
lista=[print(x) for x in thislist] # (1) "apple"  --> print(apple)
                                   # (2) "banana" --> print(banan)   
                                   # (3) "cherry" --> print(cherry)  
                                   
print(lista)

#%%

thislist = ["apple", "banana", "cherry"]
listb=[x for x in thislist]        # (1) "apple"  --> [apple]
                                   # (2) "banana" --> [apple,banana]
                                   # (3) "cherry" --> [apple,banana,cherry]
                                   
print(listb)

#%%

thislist = ["apple", "banana", "cherry"]
listc=[x.upper() for x in thislist]        # (1) "apple"  --> [apple]
                                   # (2) "banana" --> [apple,banana]
                                   # (3) "cherry" --> [apple,banana,cherry]
                                   
print(listc)


#%%

#%%

thislist = ["Apple", "Banana", "Cherry"]
listd=[x.lower() for x in thislist]        # (1) "apple"  --> [apple]
                                   # (2) "banana" --> [apple,banana]
                                   # (3) "cherry" --> [apple,banana,cherry]
                                   
print(listd)

#%%
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # 指向不同一個空間


mylist[0]="louis"

print(mylist)
print(thislist)

#%%
thislist1 = ["apple", "banana", "cherry"]
mylist1 = thislist1  # 指向同一個空間


mylist1[0]="louis"

print(mylist1)
print(thislist1)

#%%


fruits = ['apple', 'banana', 'cherry', 'banana', 'cherry', 'cherry']

x = fruits.count("cherry")

print(x)

#%%

fruits.remove("cherry")


print(fruits)


#%%


fruits = ['apple', 'banana', 'cherry', 'banana', 'cherry', 'cherry']

x = fruits.count("cherry")

print(fruits)

for i in range(x):
    fruits.remove("cherry")

print(fruits)

#%%

fruits = ['apple', 'banana', 'cherry', 'banana', 'cherry']

x = fruits.index("cherry",1)

print(x)



