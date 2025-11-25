# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:00:04 2019

@author: ASUS
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
url = 'https://shopping.pchome.com.tw/' 


browser = webdriver.Chrome()
word = '洗衣機'
All_data=[]

print('Pchome商品')
print('-------------------------------------------------')
browser.get(url)
keyword=browser.find_element(By.CLASS_NAME,'c-search__input')
keyword.clear()
keyword.send_keys(word)
keyword.send_keys(Keys.RETURN)



# 使用CLASS_NAME查找網頁元素
# 注意事項 --> 字串內有空格要改為.才能運作
# "lccnet good" >> "lccnet.good"

## 網頁上看到的Button    -->   class="btn btn--sm gtmClickV2"   請注意要把空格改成.才能運作

botton =browser.find_element(By.CLASS_NAME,'btn.btn--sm.gtmClickV2')
# botton = browser.find_element(By.CSS_SELECTOR,'btn btn--sm gtmClickV2')
# botton.click()

print("ok")

WebDriverWait(browser,10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'col3f')))

soup = BeautifulSoup(browser.page_source,'html.parser')
select_title = soup.select('h5')

while len(select_title) < 100:
    html=browser.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    select_title = soup.select('h5')

select_url = soup.select('h5 > a')
select_price = soup.find_all('span', class_='price')

index=1
for i,j,k in zip(select_title,select_url,select_price):
    print(index, i.text, k.text)
    #print(i.text, j.get('href'), k.text)
    index+=1
    #All_data.append([i.text, j.get('href'), k.text])
    
browser.close()