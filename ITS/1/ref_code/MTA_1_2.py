# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:21:05 2021

@author: OfficePC
"""

distance = float(input("請輸入以公尺為單位的行駛距離"))
distance_kms = distance / 100 #轉換為公里
time_minute = int(input("請輸入經過分鐘"))
time_sec = int(input("請輸入經過秒數"))
time=time_minute*60 + time_sec
pace = time / distance_kms
print("步速是:",str((pace//60))+":"+str((pace%60)))