# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:41:15 2023

@author: USER
"""
import re
string = '台中市南屯區埔興段35-1253號'
regex = re.compile(r'段(\d+-*\d*)(\d)(\d)')
match = regex.search(string)
print(match.group(1))

#%%

test_string='aabb abb aab dcd hab aee ab aaaaab'
pattern = 'a+b'
ans=re.findall(pattern,test_string)
print(ans)


