# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:14:31 2023

@author: USER
"""

from selenium import webdriver #匯入 webdriver 模組
browser=webdriver.Chrome() #開啟模擬瀏覽器
browser.set_window_position(100, 100)
browser.maximize_window()

browser.get("https://tw.yahoo.com/")


print(browser.name) #瀏覽器名稱
print(browser.title) #網頁標題
print(browser.current_url) #網頁 URL
browser.quit()


# print(browser.page_source) #網頁原始碼
# print(browser.session_id) #連線 ID
# print(browser.capabilities) #瀏覽器功能設定