# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 09:45:34 2025

@author: USER
"""

import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('800x800')

optionList = ['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年']   # 選項
value = tk.StringVar()                                        # 取值
value.set('')

menu = tk.OptionMenu(root, value, *optionList)                # 第二個參數是取值，第三個開始是選項，使用星號展開
menu.pack()

root.mainloop()


#%%
import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('800x800')

def show(*e):
    a.set(value.get())     # Label 變數改變成選單內容，使用 get() 取值

a = tk.StringVar()         # Label 變數
a.set('七龍珠')

label = tk.Label(root, textvariable=a)   # 建立 Label，文字為變數
label.pack()

optionList = ['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年']
value = tk.StringVar()
value.set('七龍珠')

menu = tk.OptionMenu(root, value, *optionList)  # 選單
menu.config(width=50, fg='#f00')                # 設定樣式
menu.pack()

value.trace('w', show)                          # 變數 trace 是否改變，若有改變執行 show

root.mainloop()

#%%
import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('800x800')

def show(*e):
    a.set(value.get())

a = tk.StringVar()
a.set('')

label = tk.Label(root, textvariable=a)
label.pack()

optionList = ['七龍珠','海賊王','鬼滅之刃','灌籃高手','排球少年']
value = tk.StringVar()
value.set('七龍珠')

menu = tk.OptionMenu(root, value, *optionList)
menu.config(width=50, fg='#100')
menu.pack()

button = tk.Button(root, text='顯示', command=show)
button.pack()

root.mainloop()

#%%
import os
os.chdir('C:/Users/USER/Desktop/新增資料夾')  # Colab 換路徑使用

import csv
csvfile = open('csv-demo.csv')     # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)     # 讀取 CSV 檔案
data = list(raw_data)              # 轉換成二維串列
print(data)

'''
[['name', 'id', 'color', 'price'],
 ['apple', '1', 'red', '10'],
 ['orange', '2', 'orange', '15'],
 ['grap', '3', 'purple', '20'],
 ['watermelon', '4', 'green', '30']]
'''
#%%
import csv
import openpyxl

csvfile = open('csv-demo.csv', encoding='utf-8') # 💡 建議加上 encoding='utf-8' 避免中文亂碼問題
raw_data = csv.reader(csvfile)
data = list(raw_data)
csvfile.close() # 💡 讀取完畢後應關閉檔案

wb = openpyxl.Workbook() # 建立空白的 Excel 活頁簿物件
sheet = wb.active # 💡 直接使用預設的第一個工作表 (名稱通常是 'Sheet')

for i in data:
    sheet.append(i) # 逐筆添加到最後一列

wb.save('test3.xlsx')

#%%
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
chrome_options = ChromeOptions() # 实例化 ChromeOptions 对象
# 可以在这里添加配置，例如：chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options) # 将对象传入 options 参数        # 打開瀏覽器，開啟網頁
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select    # 使用 Select 對應下拉選單
import time

# --- 【优化后的 WebDriver 初始化】 ---
# 无需指定路径，Selenium 会自动查找或下载驱动
try:
    driver = webdriver.Chrome() 
except Exception as e:
    print(f"WebDriver 初始化失败，请确保您已安装 Chrome 浏览器: {e}")
    exit()
# -----------------------------------

driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')  # 開啟範例網址

# 取得網頁元素
a = driver.find_element(By.ID, 'a')               # 取得 id 為 a 的網頁元素 ( 按鈕 A )
b = driver.find_element(By.CLASS_NAME, 'btn')     # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
c = driver.find_element(By.CSS_SELECTOR, '.test') # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, 'dog')           # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
h1 = driver.find_element(By.TAG_NAME, 'h1')       # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google') # 取得超連結文字包含 Google 的網頁元素
select_element = driver.find_element(By.XPATH, '/html/body/select')
select = Select(select_element)  # 取得 html > body > select 這個網頁元素

# 执行操作
print("--- 开始执行操作 ---")

a.click()          # 點擊 a
print(f"按鈕 A 內容: {a.text}")
time.sleep(0.5)

b.click()          # 點擊 b
print(f"按鈕 B 內容: {b.text}")
time.sleep(0.5)

c.click()          # 點擊 c
print(f"按鈕 C 內容: {c.text}")
time.sleep(0.5)

d.click()          # 點擊 d
print(f"按鈕 D 內容: {d.text}")
time.sleep(0.5)

# 執行下拉選單操作
print("選擇下拉選單的第三项 (索引 2)...")
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(0.5)

h1.click()         # 點擊 h1
print(f"點擊 H1 標題: {h1.text}")
time.sleep(0.5)

# 點擊超連結 (這將導致瀏覽器跳轉頁面)
print("點擊超連結 1 (跳轉至 Google)...")
link1.click()      # 點擊 link1
time.sleep(1) # 等待页面加载

# 返回上一個頁面以继续操作
driver.back()
time.sleep(1) # 等待返回

# 重新定位元素（因为页面可能已刷新）
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google') 

print("點擊超連結 2 (跳轉至 Oxxostudio)...")
link2.click()      # 點擊 link2

print(f"超連結 2 的 href 屬性: {link2.get_attribute('href')}")   # 印出 link2 元素的 href 屬性

# 结束
time.sleep(10)
driver.quit()
print("--- 操作结束，浏览器已关闭 ---")
#%%
import pandas as pd
import matplotlib.pyplot as plt

# 設定中文字型（以微軟正黑體為例）
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

# 模擬資料
data = {
    "姓名": ["小明", "小美", "阿志", "婷婷", "大雄"],
    "數學": [78, 95, 62, 88, 55],
    "英文": [85, 67, 90, 75, 60],
    "自然": [90, 80, 70, 95, 58]
}
df = pd.DataFrame(data)
df["總分"] = df[["數學", "英文", "自然"]].sum(axis=1)

# 畫總分柱狀圖
plt.figure(figsize=(8, 5))
plt.bar(df["姓名"], df["總分"], color='skyblue')
plt.title("同學總分比較")
plt.xlabel("姓名")
plt.ylabel("總分")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#%% --開始--批改評分使用，請勿變動
import matplotlib as mpl

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = ['Jun', 'Jul', 'Aug', 'Sep']
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, 1)
xticks = range(1, len(labels) + 1)
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks,labels)
plt.bar(labels,sizes, color="blue")

# 圓餅圖 位置
plt.subplot(1, 2, 2)
# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels,
        colors=colors, autopct='%2.1f%%')
# 長寬比為1:1
plt.axis('equal')

plt.savefig('chart.png')
plt.show()



#%%
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 讀取學生分數資料
# 讀取 read.csv
df = pd.read_csv("read.csv")
scores = df["scores"].values

# range_count[0]: range0~19
# range_count[1]: range20~39
# range_count[2]: range40~59
# range_count[3]: range60~79
# range_count[4]: range80~100
# 以0初始化計數串列
range_count = [0] * 5

# 計數過程
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

# y軸標籤
index = np.arange(0,25,5)
# X軸刻度
labels = ['0~19','0~39', '40~59','60~79', '80~100']
# 畫出長條圖
plt.bar(labels, range_count,width=0.4)
# 設定X軸名稱
plt.xlabel('Range', fontsize=14)
# 設定Y軸名稱
plt.ylabel('Quantity', fontsize=14)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('grade', fontsize=20)
# 輸出圖片檔案
plt.savefig('123.png')
plt.close()

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium.webdriver.chrome.options import Options

# 建议使用现代化的初始化方式（无需手动指定 ./chromedriver）
# 如果您坚持使用本地路径，请使用 Service 对象
# driver = webdriver.Chrome('./chromedriver') # 兼容旧版或特定环境的写法

# 现代化且推荐的写法
try:
    options = Options()
    # options.add_argument("--headless") # 可选：以无头模式运行
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"WebDriver 初始化失败：{e}")
    # 尝试使用旧版初始化方式作为后备（如果您的环境需要）
    driver = webdriver.Chrome('./chromedriver')


driver.get('https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html')

print("--- 开始滚动演示 ---")
sleep(1)
driver.execute_script('window.scrollTo(0, 500)')    # 捲動到 500px 位置
print("滚动到 500px")
sleep(1)
driver.execute_script('window.scrollTo(0, 2500)')  # 捲動到 2500px 位置
print("滚动到 2500px")
sleep(1)
driver.execute_script('window.scrollTo(0, 0)')      # 捲動到 0px 位置
print("滚动到顶部")
sleep(1)


# 1. 取得元素
h1 = driver.find_element(By.TAG_NAME, 'h1')
h3 = driver.find_element(By.TAG_NAME, 'h3')

# 2. 优化后的 JavaScript 脚本
script = '''
    let h1_element = arguments[0]; // 对应 Python 中的 h1 元素
    let h3_element = arguments[1]; // 对应 Python 中的 h3 元素
    
    // 取得元素的文本内容，并用换行符 (\n) 连接起来
    let message = "H1 Title: " + h1_element.textContent + 
                  "\\n\\n" + 
                  "H3 Title: " + h3_element.textContent;
    
    alert(message); // 弹出包含两个标题文本的提示框
'''

print("\n--- 弹出提示框 (Alert) ---")
# 3. 執行 JavaScript，弹出包含 h1 和 h3 文本内容的提示框
driver.execute_script(script, h1, h3)

sleep(2)

# 4. 处理提示框
Alert(driver).accept()    # 點擊提示視窗的確認按鈕，關閉提示視窗
print("已关闭提示框")

sleep(1)
driver.quit()
print("浏览器已关闭。")