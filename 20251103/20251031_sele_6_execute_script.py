# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:26:18 2023

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get('https://www.dcard.tw/f')
js="var action=document.documentElement.scrollTop=1000000"
driver.execute_script(js)
sleep(3)

js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)
driver.quit()
print("success")