# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:37:37 2024

@author: ronal
"""

def sumlist(l):
    if l==[]:
        return 0
    else:
        return l[0]+sumlist(l[1:])
print(sum([1,2,3,4,5]))