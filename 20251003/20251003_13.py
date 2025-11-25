# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:26:14 2020

@author: user
"""


import matplotlib.pyplot as plt

activities=["work","sleep","rest","others","reading","game"]


hours = [9,7,3,3,1,1]


colors = [(255/255,100/255,100/255),(128/255,136/255,100/255),"yellow","gray","red","blue"]
plt.title("Louis Daily")
plt.pie(hours,labels=activities,colors=colors,shadow=True,explode=(0.1,0.1,0.1,0.1,0.1,0.1),autopct="%1.2f%%")
plt.axis("equal")
plt.show()
