# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:33:08 2024

@author: ronal
"""

def multiply(m,n):
    if n==0:
        return 0
    else:
        return (m+multiply(m, n-1))
print(multiply(4,14))