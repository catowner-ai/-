# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:56:00 2022

@author: OfficePC
"""

import matplotlib.pyplot as plt
years=[1950,1960,1965,1970,1980,1985,1990,
       1995,2000,2005,2010,2015]

pops = [2.5,2.7,3.3,3,4.0,4.4,4.8,5.3,
        6.1,6.9,6.5,7.3]

deaths=[1.3,2.1,1.5,2.8,3.5,2.6,4.4,4.8,5.3,
        3.4,5.2,6.5]


plt.plot(years,pops,color=(137/255,120/255,39/255))
plt.plot(years,deaths,'--',color=(215/255,195/255,98/255))


plt.title("population growth")
plt.xlabel("population growth by year")
plt.ylabel("population in billions")
plt.show()

