# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:48:45 2023

@author: USER
"""

# message = "我是中文"
# message = message.decode('big5','replace')
# message = message.encode('utf-8')

#%%

#big5-->utf8 (method1)

inputFile = open("text_big5.txt", "r", encoding = "Big5")

outputFile = open("text_utf8.txt", "w", encoding = "UTF-8")

big5_file = inputFile.read()

outputFile.write(big5_file)

inputFile.close()
outputFile.close()

#%%

#big5-->utf8  (method2)
with open("text_big5.txt", "r", encoding = "Big5") as inputFile, open("text_utf8.txt", "w", encoding = "UTF-8") as outputFile:
    outputFile.write(inputFile.read())




#%%

#utf8-->big5 (method1)
inputFile = open("text_utf8.txt", "r", encoding = "UTF-8")

outputFile = open("text_big5.txt", "w", encoding = "Big5")

utf8_file = inputFile.read()

outputFile.write(utf8_file)

inputFile.close()
outputFile.close()
