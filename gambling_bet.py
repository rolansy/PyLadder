# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 04:46:18 2023

@author: ronal
"""

import random
import matplotlib.pyplot as plt

ACC=100
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    draw=random.randint(1,10)
    if bet==draw:
        ACC+=900-100
    else:
        ACC-=100
    y.append(ACC)
print(ACC)
plt.plot(x,y)
plt.show()
