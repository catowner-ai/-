# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:37:08 2023

@author: USER
"""

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Louis test </h2>
<p>This is a python language.</p>
<a id="Yahoo test link1" href="https://tw.yahoo.com">Yahoo link</a>
<a id="Pchome test link2" href="https://www.pchome.com.tw">Pchome link</a>
<a id="MOMO test link2" href="https://www.momo.com.tw">momo link</a>
<a id="Pchome2 test link2" href="https://www.pchome2.com.tw">Pchome2 link</a>
<a id="Pchome3 test link2" href="https://www.pchome3.com.tw">Pchome3 link</a>
<p> Hello everyone ! <b class="Boldtext"> Bold Text</b></p>
</body></html>
"""
soup=BeautifulSoup(html_doc,'html.parser')

print(soup.prettify())

title_tag=soup.title

print(soup.title)

print(title_tag)

print(title_tag.string)

#%%
a_tags=soup.find_all('a')

for tag in a_tags:
    print(tag.string)
    
#%%

for tag in a_tags:
    print(tag.get('href'))
    
#%%

tags=soup.find_all(["a","b"])
print(tags)

#%%
tags=soup.find_all(["a","b"],limit=2)
print(tags)

#%%
tags=soup.find("a")
print(tags)

