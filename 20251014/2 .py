# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:28:20 2023

@author: USER
"""

# ref : https://zh.wikipedia.org/zh-tw/HTTP%e7%8a%b6%e6%80%81%e7%a0%81
# ref : https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Reference/Status
# ref : https://requests.readthedocs.io/en/latest/api/#status-code-lookup

import requests
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

# r = requests.get('https://api.github.com/events')

r = requests.get('http://yahoo.com.tw/')

print(r.status_code)


if r.status_code == requests.codes.ok:
    print("OK")
else:
    print("crawer fail")