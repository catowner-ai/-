# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:00:12 2020

@author: user
"""


from bs4 import BeautifulSoup
import openpyxl
# encoding: utf-8
# 使用pandas處理table資料
import pandas
#台銀匯率網址
# dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
dfs = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")


#取dsf的list 資料
currency = dfs[0]
#只取前五欄
currency = currency.iloc[:,0:5]
#重新命名欄位名稱 u-utf
currency.columns = ['幣別','即期現金匯率-本行買入','即期現金匯率-本行賣出','即期現金匯率-本行買入','即期現金匯率-本行賣出']
#幣別值有重複字 利用正規式取英文代號
currency['幣別'] = currency['幣別'].str.extract('\((\w+)\)')

#將結果輸出到excel
currency.to_csv("currency.csv")
print(currency) 

currency.to_excel("currency.xlsx")