# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:23:43 2023

@author: USER
"""

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Louis test </h2>
<p>This is a python language.</p>
<a id="Yahoo test link1" href="https://tw.yahoo.com">Yahoo link</a>
<a id="Pchome test link2" href="https://www.pchome.com.tw">Pchome link</a>
<p> Hello everyone ! <b class="boldtext"> Bold Text</b></p>
<b class="lccnet bold"> Bold Text</b>
</body></html>
"""
soup=BeautifulSoup(html_doc,'html.parser')

# b_tag=soup.find_all("b")
# for i in b_tag:
#     print(i)


b_tag=soup.find_all("b",class_="bold")
print(b_tag)



#%%
import re 
b_tag=soup.find_all(class_=re.compile("^bold"))
print(b_tag)


#%%
html_doc = """
'<p class="body asfsadfa"></p>'
'<p class="sgsdfg body asfsadfa"></p>'
'<p class="body strikeout"></p>'
"""
css_soup=BeautifulSoup(html_doc,'html.parser')

# css_soup=BeautifulSoup('<p class="body strikeout"></p>','html.parser')
p_tag=css_soup.find_all("p",class_="body strikeout")
print(p_tag)


p_tag=css_soup.find_all("p",class_="body")
# print(p_tag)

for i in p_tag: 
    print(i)

#%%
p_tag=css_soup.find_all("p",class_="body strikeout")
print(p_tag)

#%%
p_tag=css_soup.find_all("p",class_="strikeout body")
print(p_tag)

#%%
# select 就是 CSS 選擇器  之後看到.後面接class name , 之後看到#指的是id=


#遇到多個 CSS class 的狀況，建議改用 CSS 選擇器來篩選
# p_tag=css_soup.select("p.strikeout.body")
p_tag=css_soup.select("p.body.strikeout")
print(p_tag)


