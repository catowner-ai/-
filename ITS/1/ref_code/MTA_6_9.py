# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:55:09 2021

@author: OfficePC
"""

def reverse_pname(backwards_pname):
    forward_pname =''
    print(len(backwards_pname))
    for index in range(len(backwards_pname)-1,-1,-1):
        #              (7-1,-1,-1)                
        forward_pname += backwards_pname[index]
        #abcdefg
    return forward_pname


print(reverse_pname("gfedcba"))

for index in range(7-1,-1,-1):
    print(index)