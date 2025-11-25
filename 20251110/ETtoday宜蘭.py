import requests

from bs4 import BeautifulSoup

import csv

import pandas as pd

r = requests.get("https://travel.ettoday.net/category/%E5%AE%9C%E8%98%AD/",verify=False)

s = BeautifulSoup(r.text, "html.parser")

#print(s.prettify())

rshref = []
rstext = []

titles = s.find_all("h3", itemprop = "headline")
for i in titles:
    rshref += [i.select_one("a").get("href")]
    #print(rshref)


titles2 = s.find_all("h3", itemprop = "headline")
for j in titles2:
    rstext += [j.select_one("a").getText()]
    #print(rstext)

ETdata = {"超連結":rshref,"介紹":rstext}
ETtoday = pd.DataFrame(ETdata)
ETtoday.to_csv("ETtoday.csv",encoding="utf8",index=False, header=True)   
