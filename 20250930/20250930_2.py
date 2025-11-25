# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:54:19 2023

@author: USER
"""

# sample_utf8.csv



# 123
# 456
# 789

import csv

fn='sample_utf8.csv'
fn1='test_ansi.csv'
with open(fn, encoding="utf-8") as csvFile:  
# with open(fn1) as csvFile:    
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
    
print(listReport)   
print("****************************")    
print(listReport[0][1],listReport[0][2])   
print(listReport[1][1],listReport[1][2])
print(listReport[2][1],listReport[2][2])
print(listReport[3][1],listReport[3][2])
csvFile.close()

#%%

import csv
fn='sample_utf8.csv'
fn1='test_ansi.csv'

with open(fn, encoding="utf-8") as csvFile:  
# with open(fn1) as csvFile:    
    csvDictReader=csv.DictReader(csvFile)
    print(csvDictReader)
    print("****************************")    
    print(type(csvDictReader))
    print("****************************") 
    for row in csvDictReader:
        # print(row)
        print(row['速度'],row['高度'])
  
        # print(row['速度'])
        # print(row['高度'])
        
csvFile.close()
#%%

import csv
fn ='APPLE5_1.csv'      
        
with open(fn,'w',newline='') as csvFile:
# with open(fn,'w') as csvFile:
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(['姓名','電話','ID'])
    csvWriter.writerow(['小強','02-25632145','A123456789'])
    csvWriter.writerow(['lccnet','04-65214756','B987654321'])
csvFile.close()

#%%

# Dictreader 
with open(fn, encoding="utf-8") as csvFile:  
# with open(fn1) as csvFile:    
    csvDictReader=csv.DictReader(csvFile)
    print(csvDictReader)
    print(type(csvDictReader))
    print("****************************") 
    print(csvDictReader.fieldnames)  #欄位名稱
    print("****************************") 
    for row in csvDictReader:
        
        # print(row)
        # print(row['電話'])
        # print(row['ID'])
        print(row['姓名'],row['電話'],row['ID'])
#%% 查詢預設編碼值

import locale
print(locale.getpreferredencoding()) 
        
#%%
#reader 
with open(fn, encoding="utf-8") as csvFile:  
# with open(fn1) as csvFile:    
    csvReader=csv.reader(csvFile)
    
    print(csvReader)
    
    for row in csvReader:
        print("Row %s=" %csvReader.line_num,row)
 
        
 #%%

import csv
fn ='APPLE6.csv'      
         
with open(fn,'w', encoding="Big5") as csvFile:
     csvWriter=csv.writer(csvFile)
     csvWriter.writerow(['姓名','電話','ID'])
     csvWriter.writerow(['小強','02-25632145','A123456789'])
     csvWriter.writerow(['lccnet','04-65214756','B987654321'])
csvFile.close()
    
 
    
        
#%%

import csv
fn ='sony.csv'      
        
with open(fn,'w',newline='', encoding="utf-8") as csvFile:
    csvWriter=csv.writer(csvFile,delimiter='\t')
    csvWriter.writerow(['姓名','電話','ID'])
    csvWriter.writerow(['李小明','02-25632145','A123456789'])
    csvWriter.writerow(['張小華','04-65214756','B987654321'])
    
 #%%
    
import csv
fn='csv_output_dict.csv'
with open(fn,'w',newline='')as csvFile:  
    
    
    
    fields=['姓名','電話','ID']
    dictWriter=csv.DictWriter(csvFile,fieldnames=fields)
    dictWriter.writeheader()
    dictWriter.writerow({'姓名':"李小明","電話":"02-123456","ID":"A123456789"})
    dictWriter.writerow({'姓名':"小白","電話":"02-123456","ID":"B987654321"})
    
#%%

    #%%
    
import csv

dictList=[{'姓名':"李小明","電話":"02-123456","ID":"A123456789"},
          {'姓名':"小白","電話":"02-123456","ID":"B987654321"}]
fn='csv_output_dict2.csv'
with open(fn,'w',newline='')as csvFile:  
    
    fields=['姓名','電話','ID']
    dictWriter=csv.DictWriter(csvFile,fieldnames=fields)
    dictWriter.writeheader()
  
    for row in dictList:
        dictWriter.writerow(row)
    # dictWriter.writerow({'姓名':"李小明","電話":"02-123456","ID":"A123456789"})
    # dictWriter.writerow({'姓名':"小白","電話":"02-123456","ID":"B987654321"})
    
    
#%%

import csv
# 開啟 CSV 檔案
inputfn='csv_sample.csv'  # reader file

outfn='csv_output_writer.csv'   #write file


with open(inputfn, newline='',encoding="utf-8") as csvFile:
    rows=csv.reader(csvFile)
    listReport=list(rows)








with open(outfn,'w',newline='')as csvFile:
    csvWriter=csv.writer(csvFile)
    for row in listReport:
        csvWriter.writerow(row)
        
 #%%

# utf-8-sig 的主要特點
# 帶有BOM的UTF-8： 它的全稱是"UTF-8 with Byte Order Mark"。 
# 識別編碼： BOM位於文件開頭，是一個不可見的字元序列，用於告訴讀取軟體該文件採用的是UTF-8編碼。 
# 解決亂碼問題： 它能幫助軟體，特別是Windows上的應用程式，準確地識別文件的編碼，進而避免中文內容顯示成亂碼。 
# 自動處理： 在Python中，使用`open()函式指定encoding='utf-8-sig'`時，讀取檔案會自動忽略BOM（如果存在），而寫入檔案時則會自動加上BOM。 

# import csv  


      
import csv
inputfn='csv_sample.csv'  # reader file

with open(inputfn, newline='',encoding="utf-8-sig")as f:
    data=[k for k in csv.reader(f)]

with open('out.csv','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerows(data)
    
print(data[1][0])

print(data[1][0]*2)  

print(float(data[1][0])*2)
    
    
 #%%
'''  

寫入CSV檔時遇到亂碼問題，可將編碼設置為utf-8-sig而非utf-8。

utf-8-sig能正確處理BOM，確保Excel能正常打開無亂碼。

utf-8不包含BOM，可能會導致讀取時出錯

編碼BOM (Byte Order Mark, 位元組順序標記) 是一個位於統一碼字元U+FEFF 的特殊字元，

用於在檔開頭標示其所使用的字元編碼（如UTF-8、UTF-16、UTF-32）和位元組序（只在UTF-16 和UTF-32 中存在）。 

'''




