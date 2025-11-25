# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:19:15 2021

@author: OfficePC
"""

while True:
    try:
        x = int(input("請問您有幾隻寵物呢??"))
        break
    except ValueError:
        print("寵物沒有小數點啦,請輸入整數")