# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:32:18 2023

@author: USER
"""

from selenium import webdriver #匯入 webdriver 模組
browser=webdriver.Chrome() #開啟模擬瀏覽器



urls=["http://www.google.com.tw", "http://tw.yahoo.com", "https://www.lccnet.com.tw"] #URL 串列
for url in urls: #依序開啟網頁 (最後停在 lccnet)
    browser.get(url)
    
print(browser.current_url) #最後停在 lccnet


browser.back() #回前一頁 (YAHOO)
print(browser.current_url)

browser.back() #回前一頁 (Google)
print(browser.current_url)


browser.forward() #回後一頁 (YAHOO)
print(browser.current_url)


browser.forward() #回後一頁 (lccnet)
print(browser.current_url)


browser.refresh() #重新載入

browser.quit()