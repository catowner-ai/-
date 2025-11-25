# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:19:07 2023

@author: USER
"""

# 山東艦
from selenium import webdriver

from selenium.webdriver.common.by import By

url='https://tw.yahoo.com/'

# driver_path = r'C:\Users\USER\Desktop\chromedriver.exe'
# chrome = webdriver.Chrome(driver_path)

driver=webdriver.Chrome()
driver.set_page_load_timeout(360) # Set to 240 seconds (4 minutes)
driver.get(url)

elem = driver.find_element(By.ID, "header-search-input")
elem.send_keys('金鐘獎頒獎典禮')


sumbit=driver.find_element(By.ID, "header-desktop-search-button").click()
# driver.quit()

#%%
# url --> https://24h.pchome.com.tw/
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url='https://24h.pchome.com.tw/'

driver=webdriver.Chrome()
driver.get(url)

elem = driver.find_element(By.CLASS_NAME, "c-search__input")


# elem.send_keys('金鐘獎頒獎典禮')

elem.send_keys('iphone17')
elem.send_keys(Keys.RETURN)

# sumbit=driver.find_element(By.CLASS_NAME, "btn btn--sm gtmClickV2").click()

#%%
# url --> https://www.pchome.com.tw/
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url='https://www.pchome.com.tw/'

driver=webdriver.Chrome()
driver.get(url)

elem = driver.find_element(By.ID, "ecsearch_value")

elem.clear()
elem.send_keys('金鐘獎頒獎典禮')
elem.send_keys(Keys.RETURN)

    
# elem.send_keys('iphone17')


# sumbit=driver.find_element(By.CLASS_NAME, "search-btn flt-right").click()





