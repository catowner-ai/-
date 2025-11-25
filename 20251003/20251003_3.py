# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:58:26 2022

@author: OfficePC
"""

import matplotlib.pyplot as plt


years=[1950,1960,1965,1970,1980,1985,1990,
       1995,2000,2005,2010,2015]
print(len(years))




pops = [2.5,2.7,3.3,3,4.0,4.4,4.8,5.3,
        6.1,6.9,6.5,7.3]
print(len(pops))

plt.plot(years,pops,"g")


plt.title("population growth")
plt.xlabel("population growth by year")
plt.ylabel("population in billions")
plt.show()
