# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:11:08 2021

@author: OfficePC
"""

ontime = input("車子是在晚上 11 點前歸還的嗎? y 或 n").lower()
days_rented = int(input("車子出租了幾天?"))
day_rented = input("車子是在星期幾出租?").capitalize()
cost_per_day = 100
if ontime =="n":
    days_rented+=1
if day_rented =="Sunday":
    Total = (days_rented * cost_per_day)*0.9
elif day_rented =="Thursday":
    Total = (days_rented * cost_per_day) *0.8
else:
    Total = days_rented * cost_per_day
print("車輛的租借費用為: $",Total)