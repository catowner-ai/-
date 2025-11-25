# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:38:21 2020

@author: user
"""

#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(np.random.randn(6,6),index = list('QWERTY'),columns=list('ZXCVBN'))

# df.plot()
# plt.show()

x=[70,80,90,100,110,120,130,140,150]
x1=[60,50,80,105,120,118,126,150,165]

y=[2.2,3.3,10.7,5.4,12.8,17.6,11.2,5.6,15.7]
tl=["<75","75-84","85~94","95~104","105~114","115~124","125~134","135~144",">144"]


plt.figure(figsize=(8,4))


plt.bar(x,width=3,label="Sample1",height=y,color=(160/255,100/255,180/255))
plt.bar(x1,width=5,label="Sample2",height=y,color=(120/255,160/255,180/255))

plt.legend()

plt.xlabel("Smarts")
plt.ylabel("Probability(%)")
plt.title("Bar of IQ")

plt.show()
