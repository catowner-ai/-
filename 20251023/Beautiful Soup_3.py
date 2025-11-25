# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:19:38 2023

@author: USER
"""

from bs4 import BeautifulSoup

html_doc="""
<html>
   <head>
       <title>Hello World</title></head>
<body><h2>Louis test </h2>
<p>This is a python language.</p>
<div data-foo="value">foo!</div>
<a id="Yahoo test link1" href="https://tw.yahoo.com">Yahoo link</a>
<a id="Pchome test link2" href="https://www.pchome.com.tw">Pchome link</a>
<a id="Pchome test link3" href="https://www.pchome.com.tw">Pchome link</a>
<div data-foo="value">foo!</div>
<p> Hello everyone ! <b class="Boldtext"> Bold Text</b></p>
<div data-foo="value">foo!</div>
</body></html>
"""
data_soup=BeautifulSoup(html_doc,'html.parser')



# data_soup=BeautifulSoup('<div data-foo="value">foo!</div>','html.parser')


# #Error
# data_soup.find_all(data-foo="value")

#Success
data=data_soup.find_all(attrs={"data-foo":"value"})
for tag in data:
    print(tag)