# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:52:13 2023

@author: USER
"""

# ref : https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_common/selenium.webdriver.common.keys.html

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://www.python.org")
elem = driver.find_element(By.NAME, "q")



elem.clear()
elem.send_keys("pandas")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()