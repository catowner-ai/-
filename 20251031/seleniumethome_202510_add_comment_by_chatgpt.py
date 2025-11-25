# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:13:29 2023
@author: USER
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


# ================================
#  用來存放爬取後資料的清單
# ================================
date_list = []     # 商品促銷日期
title_list = []    # 商品名稱
price_list = []    # 最終價格
url_list = []      # 商品網址
prices_list = []   # 原始價格字串清單


# ================================
#  設定 Chrome Options
# ================================
options_obj = webdriver.ChromeOptions()

# 允許通知（可不加）
params = {
    'profile.default_content_setting_values': {
        'notifications': 1
    }
}
options_obj.add_experimental_option('prefs', params)

# 移除「自動測試」提示banner
options_obj.add_experimental_option('excludeSwitches', ['enable-automation'])
options_obj.add_argument("--disable-infobars")  # 修正原本的語法錯誤


# ================================
#  啟動 Chrome
# ================================
browser = webdriver.Chrome(options=options_obj)


# ================================
#  前往 ETMall 商品頁面
# ================================
browser.get("https://www.etmall.com.tw/c3/78532")

# 等待 HTML 內容載入（ETMall 有些資料是 JS 動態載入）
time.sleep(2)


# ================================
#  使用 BeautifulSoup 解析頁面
# ================================
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 促銷日期（如：限時 2/1 - 2/3）
date_tags = soup.select('p.n-sale--subtitle')
print("Date tags:", date_tags)

# 商品名稱 + 連結
title_tags = soup.select('p.n-name a')
print("Titles:", title_tags)

# 商品價格（class = n-final-price）
price_tags = soup.find_all('span', class_='n-final-price')
print("Prices:", price_tags)


# ================================
#  清理價格文字，例如 "$12,400" → "$12,400"
# ================================
prices_list = [p.get_text(strip=True) for p in price_tags]
print("Final price list:", prices_list)


# ================================
#  組合資料（用 zip 同時迭代三個 list）
# ================================
for d, t, p in zip(date_tags, title_tags, prices_list):

    # 促銷日期
    date_list.append(d.get_text(strip=True))

    # 商品名稱
    title_list.append(t.get_text(strip=True))

    # 商品網址（加上主網域）
    url_list.append("https://www.etmall.com.tw" + t.get('href'))

    # 最終價格
    price_list.append(p)


# ================================
#  印出結果
# ================================
print("\n--- Extracted Data ---")
print("Dates:", date_list)
print("Titles:", title_list)
print("URLs:", url_list)
print("Prices:", price_list)


# ================================
#  關閉瀏覽器
# ================================
browser.quit()
