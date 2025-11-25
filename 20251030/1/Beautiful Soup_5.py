# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:31:59 2023

@author: USER
"""

from bs4 import BeautifulSoup
import re 


links_html="""
<a id="link1" href="/my_link1">link One</a>
<a id="link2" href="/my_link2">link Two</a>
<a id="link3" href="/my_link3">link Three</a>
"""

soup=BeautifulSoup(links_html,'html.parser')

soup.find_all("a" , string="link One")

#%%
soup.find_all("a",string=re.compile("^link"))

#%%

from bs4 import BeautifulSoup
import re 

#example 1
html_doc2="""
<body>
    <p class="apple">
            <a id="link11" href="/my_link11">link One1</a>
            <a id="link12" href="/my_link12">link One2</a>
            <a id="link13" href="/my_link13">link One3</a>
            
            <a id="link2" href="/my_link2">link Two</a>
            <a id="link3" href="/my_link3">link Three</a>
            <a id="link4" href="/my_link3">link Four</a>
     </p>

</body>
"""

# # example 2 
# html_doc2="""
# <body>
#     <p class="apple">
#             <a id="link11" href="/my_link11">link One1</a>
#             <a id="link12" href="/my_link12">link One2</a>
#             <a id="link13" href="/my_link13">link One3</a>
     
#          <p class="iphone17">    
#             <a id="link2" href="/my_link2">link Two</a>
#             <a id="link3" href="/my_link3">link Three</a>
#             <a id="link4" href="/my_link3">link Four</a>
#          </p> 
#    </p>
# </body>
# """

soup=BeautifulSoup(html_doc2,'html.parser')

link2_tag=soup.find(id='link2')

p_tag=link2_tag.find_parents("p")

print(p_tag)

#%%

#同一層往前找
link_tag=link2_tag.find_previous_siblings("a")
print(link_tag)

#%%

#同一層往後找
link_tag=link2_tag.find_next_siblings("a")
print(link_tag)


#%%

from bs4 import BeautifulSoup

with open("test.html",encoding='utf-8') as f:
    soup = BeautifulSoup(f,'html.parser')
    print(soup.prettify())
    
    
    
    