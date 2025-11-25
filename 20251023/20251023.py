# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:53:27 2023 .3

@author: USER
"""

# ref : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# ref : https://beautifulsoup.cn/

html_doc = """
<html>
<head><title>The Lccnet's story</title></head>
<body>
<p class="title"><b class="boldtext app louis">The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie111</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie222</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie333</a>;
and they lived at the bottom of a well.</p>
<a href="http://www.yahoo.com.tw" class="sister" id="yahoo">雅虎</a>,
<a href="http://www.yahoo.com.tw" class="brother" id="yahoo2">奇摩</a>,
<a href="http://www.pchome.com.tw" class="sister" id="pchome">網路家庭</a> and
<a href="http://www.lccnet.com.tw" class="lccnet" id="lccnet">聯成</a>
<a href="http://tw.lccnet.com" class="lccnet2" id="lccnet">聯成2</a>
<p class="title"><b class="louis">louis</b></p>
<p class="title"><b class="app louis">app</b></p>

<p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"lxml")


# soup = BeautifulSoup(open("test.html"),"lxml")

#輸出排版後網頁程式碼
print(soup.prettify())

#%%

#抓出title此標籤的節點
title_tag=soup.title


#印出title此標籤的節點 含標籤內容
print(title_tag)

#印出title此標籤的節點 「不含」標籤內容，只有文字
print(title_tag.string)



#%%
#抓出a此標籤的節點
a_tag=soup.a

#印出a此標籤的節點 含標籤內容
print("a_tag = ",a_tag)

print("********************")

#印出a此標籤的節點 「不含」標籤內容，只有文字
print("a_tag.string = ",a_tag.string)
#%%

#抓出a此標籤的所有節點
a_tags = soup.find_all('a')

#逐個列印a此標籤的節點
for tag in a_tags:
    print(tag.string)  #逐個列印a此標籤的節點文字
    print(tag.get('id'))  #逐個列印a此標籤的id
    print(tag.get('href')) #逐個列印a此標籤的href
    
#%%    
a_tags = soup.find_all(['a','b'])   #找出所有a或b此標籤的節點含標籤內容


#逐個列印a或b標籤的節點
for tag in a_tags:
    print(tag) #印出a或b此標籤的節點含標籤內容
    print(tag.string)#印出a或b此標籤的節點 不含標籤內容，只有文字
    print(tag.get('href'))#印出a或b此標籤的節點href
    
    
    
#%%
a_tags = soup.find_all(['a','b'],limit=6) #找出所有a或b此標籤的節點含標籤內容, 「限定6筆資料」
for tag in a_tags:
    print(tag) #印出a或b此標籤的節點含標籤內容
    print(tag.string)#印出a或b此標籤的節點 不含標籤內容，只有文字
    print(tag.get('href'))#印出a或b此標籤的節點href
    
#%%
a_tags = soup.find_all(['a','b'],limit=4,recursive=True)
for tag in a_tags:
    print(tag)
    print(tag.string)
    print(tag.get('href'))  
#%%
#id來做查找的方式
link2_tags = soup.find(id='yahoo') 
print(link2_tags)


#%%
#id來做查找的方式
link4_tags = soup.find(id='lccnet') 
print(link4_tags)

#%%

#抓出a此標籤的所有節點, 但有限定要href='http://www.yahoo.com.tw'
a_tag=soup.find_all("a",href='http://www.yahoo.com.tw')
print(a_tag) 



#%%


# ref : https://docs.python.org/zh-tw/3/library/re.html

#搭配正則表示式來找尋特定條件的資料
import re
links=soup.find_all(href=re.compile("www"),id="lccnet")
print(links) 



#%%

b_tag=soup.find_all("b",class_="Boldtext")  # 等同於去查找網頁語言裡的class="Boldtext" 大小寫文字是有區分的
print(b_tag)

print("**********************************")

a_tag=soup.find_all("a",class_="lccnet")   # 等同於去查找網頁語言裡的class="lccnet"  大小寫文字是有區分的
print(a_tag)

#%%

b_tag=soup.find_all("b",class_=re.compile("^bold"))  #符合字串的開頭
print(b_tag)

#%%


#class_找尋方式是以單詞的找尋方式

b_tag=soup.find_all("b",class_="boldtext")
print(b_tag)

b_tag=soup.find_all("b",class_="app")
print(b_tag)

b_tag=soup.find_all("b",class_="louis")
print(b_tag)

#class_找尋方式也支援完整的內容找尋方式
b_tag=soup.find_all("b",class_="boldtext app louis")
print(b_tag)


#class_找尋方式也支援完整的內容找尋方式,順序要正確
b_tag2=soup.find_all("b",class_=" app boldtext louis")
print(b_tag2)

#%%
#css select
#<b class="boldtext app">The Dormouse's story</b>

#以下三個語法都找到同組資料
# b_tag=soup.select("b.app.boldtext.louis")
# b_tag=soup.select("b.boldtext.app.louis")
b_tag=soup.select("b.louis.boldtext.app")

print(b_tag)


#以下語法找到二組資料，只要符合內容有app , louis即可
b_tag=soup.select("b.app.louis")
print(b_tag)

#%%

#此範例是用抓出a或b標籤並找出文字內容符合的資料
links_html="""
<a id ="link1" href="/my_link1">Link One</a>
<a id ="link2" href="/my_link2">Link Two</a>
<a id ="link3" href="/my_link3">Link Three</a>
<a id ="link4" href="/my_link4">Link Four</a>

<b id ="link4" href="/my_link4">Link Three</b>
<b id ="link41" href="/my_link41">Link Three</b>
<b id ="link42" href="/my_link42">Link Three</b>
"""
soup = BeautifulSoup(links_html,"lxml")

# a_tags=soup.find_all("a",string="Link Three")
# for tag in a_tags:
#     print(tag)


b_tags=soup.find_all("b",string="Link Three")
for tag in b_tags:
    print(tag)
