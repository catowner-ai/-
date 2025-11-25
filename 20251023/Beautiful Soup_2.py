# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:02:07 2023

@author: USER
"""

from bs4 import BeautifulSoup

html_doc = """
<html>
   <head>
       <title>Hello World</title></head>
<body><h2>Louis test </h2>
<p>This is a python language.</p>
<a id="Yahoo test link1" href="https://tw.yahoo.com">Yahoo link</a>
<a id="Pchome test link2" href="https://www.pchome.com.tw">Pchome link</a>
<a id="Pchome test link3" href="https://www.pchome.com.tw">Pchome link</a>
<p> Hello everyone ! <b class="Boldtext"> Bold Text</b></p>
</body></html>
"""
soup=BeautifulSoup(html_doc,'html.parser')


print(soup.prettify())

title_tag=soup.title

print(soup.title)

print(title_tag)

print(title_tag.string)


soup.find_all("title")

soup.find_all("title",recursive=False)

#%%

link2_tag=soup.find(id='Yahoo test link1')
print(link2_tag)

#%%

#特定資料的查找
a_tag=soup.find_all("a",href="https://tw.yahoo.com")
print(a_tag)


#所有的a tag 都查找
a_tag=soup.find_all("a")

for i in a_tag:
    print(i)

#%%

import re 
links = soup.find_all(href=re.compile("pchome"))
print(links)

#%%

import re 
links = soup.find_all(href=re.compile("pchome"),id="Pchome test link2")
print(links)
