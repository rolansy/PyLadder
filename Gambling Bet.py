# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 04:46:18 2023

@author: ronal
"""

import random

acc=100
for i in range(365):
    bet=random.randint(1,10)
    draw=random.randint(1,10)
    if bet==draw:
        acc+=900-100
    else:
        acc-=100
print(acc)