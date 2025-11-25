# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 18:14:27 2025

@author: USER
"""

# -*- coding: utf-8 -*-
"""
bsyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.myweb.tw/python.png">
      <a href="http://www.my-web.com.tw">超連結1</a>
      <img src="http://www.lccnet.com.tw/test.png">
      <a href="http://www.lccnet.com.tw">超連結2</a>
      <img src="http://www.ntu.edu.tw/python.png">
      <a href="http://www.ntu.edu.tw">超連結3</a>
      <img clsss="abc">
      <div class="title">		
          <a href="https://tw.news.yahoo.com/apec%E5%B3%B0%E6%9C%83%E5%8D%97%E9%9F%93%E7%99%BB%E5%A0%B4-%E6%9E%97%E4%BF%A1%E7%BE%A9%E9%80%B2%E5%A0%B4%E5%A4%A7%E6%9C%83%E8%BD%89%E6%92%AD%E7%95%AB%E9%9D%A2%E7%A7%80%E3%80%8Ctaiwan%E3%80%8D%E5%8F%8A%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%97%97-015541554.html">APEC峰會南韓登場 林信義進場大會轉播畫面秀「Taiwan」及中華民國國旗</a>		
      </div>
      
      
  </body>
</html>
'''
bs = BeautifulSoup(html, 'html.parser')

# temp=bs.select("img.src")
# print(temp)


#第一組資料方法一
print(bs.select('img')[0].get('src'))
print(bs.select('a')[0].get('href'))

#第一組資料方法二
print(bs.select('img')[0]['src'])
print(bs.select('a')[0]['href'])


#第二組資料方法一
print(bs.select('img')[1].get('src'))
print(bs.select('a')[1].get('href'))
#第二組資料方法二
print(bs.select('img')[1]['src'])
print(bs.select('a')[1]['href'])

#第三組資料方法一
print(bs.select('img')[2].get('src'))
print(bs.select('a')[2].get('href'))

#第三組資料方法二
print(bs.select('img')[2]['src'])
print(bs.select('a')[2]['href'])