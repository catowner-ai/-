# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:34:51 2025

@author: USER
"""

import requests
res = requests.get('http://pala.tw/js-example/')
print(res.text)