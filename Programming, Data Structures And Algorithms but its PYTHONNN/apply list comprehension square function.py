# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:44:40 2024

@author: ronal
"""

def applylist(f,l):
    for i in range(len(l)):
        l[i]=f(l[i])
    return l
def f(x):
    return x**2

l=list(range(2,100,6))
l=applylist(f, l)