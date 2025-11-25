# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:56:29 2021

@author: OfficePC
"""

member = open('apple.txt','r')
eof = False
while eof == False:
    line = member.readline()
    if line !='':
      if line !="\n":
            print(line.strip())
    else:
        print("檔案結束")
        eof = True
member.close()