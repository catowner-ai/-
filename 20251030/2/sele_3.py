# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:23:11 2023

@author: USER
"""

from selenium import webdriver #匯入 webdriver 模組
browser=webdriver.Chrome() #開啟模擬瀏覽器
print(browser.get_window_position())
browser.set_window_position(50, 100)
print(browser.get_window_position())


print(browser.get_window_size())
browser.set_window_size(1024, 768)
print(browser.get_window_size())


browser.maximize_window()
print(browser.get_window_size())


browser.minimize_window()
print(browser.get_window_size())