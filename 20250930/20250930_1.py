# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:34:05 2023

@author: OfficePC
"""

import csv

fn='test.csv'
fn1='test_ansi.csv'
fn2="sample_ansi.csv"
fn3="sample_utf8.csv"


# with open(fn3, encoding="utf-8") as csvFile:  
with open(fn2, encoding="big5") as csvFile:    
    csvReader=csv.reader(csvFile)
    # print("before")
    print("csv_reader = ",csvReader)
    listReport=list(csvReader)
    print("list_report= ",listReport)
    # print("after")
    # print(csvReader)
    # csvReader=csv.reader(csvFile)
    # for row in csvReader:
    #     print(row)
    #     print("Row %s=" %csvReader.line_num,row)
      
# print(type(listReport))
# print(listReport)

#%%


import csv

fn='sample_utf8.csv'
# fn1='test_ansi.csv'
with open(fn) as csvFile:  
# with open(fn1) as csvFile:    
    csvReader=csv.reader(csvFile)
    for row in csvReader:
        print("Row %s=" %csvReader.line_num,row)

#%%

import csv

fn='sample_utf8.csv'
fn1='sample_utf8.csv'
with open(fn, encoding="utf-8") as csvFile:  
# with open(fn1) as csvFile:    
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
    #          list(1,2,3,4,5,6)
for row in listReport:
    print(row)
