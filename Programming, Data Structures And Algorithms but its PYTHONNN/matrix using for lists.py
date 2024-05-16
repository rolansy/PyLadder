# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:23:13 2024

@author: ronal
"""

m=[[i*j for i in range(3)]for j in range(3)]
print(m)

z=[0 for i in range(3)]
l=[z for i in range(4)]
print(l)
l[1][2]=6
print(l)