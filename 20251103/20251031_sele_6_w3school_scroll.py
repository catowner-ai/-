# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:42:30 2023

@author: USER
"""

# ref : https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/ui/WebDriverWait.html
# ref : https://selenium-python-zh.readthedocs.io/en/latest/waits.html


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.w3schools.com')
target=driver.find_element(By.LINK_TEXT,'Play Game')

actions=ActionChains(driver)
actions.move_to_element(target)
actions.perform()
sleep(3)
# driver.quit()
print('success')

#%%


from selenium import webdriver

from selenium.webdriver.common.by import By

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.w3schools.com')

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
sleep(3)


# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
# sleep(3)
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
# sleep(3)
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
# sleep(3)

# driver.quit()
print('success')