# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:17:47 2024

@author: ronal
"""

l=[ (x,y,z) for x in range(1,100) for y in range(1,100) for z in range(1,2100) if x**2+y**2==z**2]
print(l)