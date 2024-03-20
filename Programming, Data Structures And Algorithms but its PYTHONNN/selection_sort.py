# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:45:31 2024

@author: ronal
"""

def selectionsort(l):
    for start in range(len(l)):
        minpos=start
        for j in range(start,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        l[start],l[minpos]=l[minpos],l[start]
    return l
l=list(map(int,input("Enter List : ").split()))
print(selectionsort(l))
                