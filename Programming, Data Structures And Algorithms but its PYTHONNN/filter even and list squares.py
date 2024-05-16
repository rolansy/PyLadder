# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:04:28 2024

@author: ronal
"""

def square(x):
    return x**2
def iseven(x):
    return x%2==0

l=list(map(square,filter(iseven,range(2,20,3))))
f=list(filter(iseven,range(5,60)))