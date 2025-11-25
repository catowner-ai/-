# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:15:46 2021

@author: OfficePC
"""
Nowvalue=0


def calculator_value(Nowvalue, getpoint):
    Nowvalue += getpoint
    return Nowvalue



final_value=calculator_value(Nowvalue,10)
print(final_value)

