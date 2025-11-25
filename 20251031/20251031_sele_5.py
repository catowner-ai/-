# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:20:03 2023

@author: USER
"""

# ref : https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.ui.html

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')


driver=webdriver.Chrome()
driver.get(r"C:\Users\Louis\Desktop\20251020\TEST_URL.html")

select=Select(driver.find_element(By.NAME,'select_name'))

sleep(5)

select_index_value=select.select_by_index(5)

print(select_index_value)

sleep(5)

select_value_value=select.select_by_value("cat")


sleep(5)

select_visible_text=select.select_by_visible_text(u"Parrot")

for op in select.options:
    print(op.text)
    