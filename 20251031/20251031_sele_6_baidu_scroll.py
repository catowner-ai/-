# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:33:12 2023

@author: USER
"""

# https://selenium-python.readthedocs.io/api.html
# https://www.w3schools.com/js/DEFAULT.asp


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get('https://www.baidu.com')
driver.find_element(By.ID,'chat-textarea').send_keys('selenium')


driver.find_element(By.ID,'chat-submit-button').click()

# wait
sleep(3)


js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(3)

js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)

js="var action=document.documentElement.scrollTop=50"
driver.execute_script(js)
sleep(3)

driver.quit()
print("success")