# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:50:05 2023

@author: USER
"""

# ref : https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/ui/WebDriverWait.html
# ref : https://selenium-python-zh.readthedocs.io/en/latest/waits.html


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from selenium.webdriver.support.ui import Select
# from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.get('https://www.csdn.net/?ydreferer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%3D')
locator=(By.LINK_TEXT,'AI原生软件研发成熟度地图')
print(locator)

try:
    print("selenium test")
    WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located(locator))
    print(driver.find_element(By.LINK_TEXT('AI原生软件研发成熟度地图')).get_attribute('href'))
except:  #執行try區塊的內容如果 「有」發生錯誤，會執行except
    print("error occur")
    
    
else:   #執行try區塊的內容如果「沒有」發生錯誤，會執行else
    print("ok")  
    

finally:  #執行try區塊的內容不管「有沒有」發生錯誤，都會執行finally
    driver.close()
    
 #因為有寫try except所以不管有無爬到資料，程式就可以繼續往下運作   
print("lccnet")   

#%%



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://www.google.com.tw')




# #2行寫法
# #最長等10秒，每隔1秒一次確認一次要找的tag出現了沒，設定方式為下一行​
# driver_wait = WebDriverWait(driver,10,1)

# #顯性等待抓取元素​，設定要找的tag 對象
# search_box = driver_wait.until(EC.presence_of_element_located((By.NAME,"q")))





# #1行寫法
# WebDriverWait(driver, 10,1).until(EC.presence_of_element_located((By.NAME,"q")))



try:
    print("find q")
    WebDriverWait(driver, 10,1).until(EC.presence_of_element_located((By.NAME,"q")))
    
    
except:  #執行try區塊的內容如果 「有」發生錯誤，會執行except
    print("error occur")
    
    
else:   #執行try區塊的內容如果「沒有」發生錯誤，會執行else
    print("find q ok")  
    

finally:  #執行try區塊的內容不管「有沒有」發生錯誤，都會執行finally
    driver.close()
    
 #因為有寫try except所以不管有無爬到資料，程式就可以繼續往下運作   
print("lccnet")   



