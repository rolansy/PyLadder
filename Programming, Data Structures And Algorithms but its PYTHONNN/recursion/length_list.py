# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:35:36 2024

@author: ronal
"""

def llength(l):
    if l==[]:
        return 0
    else:
        return (1+llength(l[1:]))
print(llength([1,2,3,4,5]))