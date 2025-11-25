# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:42:29 2023

@author: USER
"""

# ref : https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/ui/WebDriverWait.html
# ref : https://selenium-python-zh.readthedocs.io/en/latest/waits.html


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()


driver.get('http://www.pchome.com.tw')

sleep(20)

print(driver.current_url)
driver.quit()

#%%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get('http://www.pchome.com.tw')

print(driver.current_url)
driver.quit()