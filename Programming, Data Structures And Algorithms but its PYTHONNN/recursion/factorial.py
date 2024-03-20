# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:36:47 2024

@author: ronal
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))