# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:46:17 2023

@author: USER
"""
# chrome dirver : https://github.com/dreamshao/chromedriver

# driver_path = r'C:\Users\USER\Desktop\sele\chromedriver.exe'
# chrome = webdriver.Chrome(driver_path)
# chrome.get("http://www.google.com")

from selenium import webdriver #載入 webdriver 模組
browser=webdriver.Chrome() #建立瀏覽器物件
browser.get("http://tw.yahoo.com")

browser.quit()