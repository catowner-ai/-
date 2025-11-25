# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:40:20 2023

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


lista=[]
options = webdriver.ChromeOptions()

options.add_argument('--headless')  # 設定動態爬蟲在背景執行

url='https://tw.yahoo.com/'


#未加入options
# driver=webdriver.Chrome()


#加入options
driver=webdriver.Chrome(options=options)

# driver.implicitly_wait(5)  # 最長等5秒，如果提早完成網頁載入，就馬上往下執行


driver.get(url)


# 分二行的寫法
# elem = driver.find_element(By.ID, "header-search-input")
# elem.send_keys('豪雨')

# 一行的寫法
elem = driver.find_element(By.ID, "header-search-input").send_keys('豪雨')



sumbit=driver.find_element(By.ID, "header-desktop-search-button").click()

# driver.implicitly_wait(15)

# sleep(15)  #一定會等5秒才繼續往下


# element = WebDriverWait(driver,5).until(
#     expected_conditions.presence_of_element_located((By.ID,'web'))
#     )



soup=BeautifulSoup(driver.page_source,"html.parser")

links=soup.select('div#web h3')
for link in links:
    print(link.get_text())
    lista.append(link.get_text())
print(lista)
driver.close()