# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:23:29 2024

@author: ronal
"""

def insertionsort(l):
    for slice_end in range(len(l)):
        pos=slice_end
        while pos>0 and l[pos]<l[pos-1]:
            l[pos],l[pos-1]=l[pos-1],l[pos]
            pos-=1
    return l
l=list(range(4,50,2))
from random import shuffle
shuffle(l)
print(insertionsort(l))