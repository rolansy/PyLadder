# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:42:25 2024

@author: ronal
"""

def insertion_sort_recursive(l):
    isort(l,len(l))
    return l
def isort(l,k):
    if k>1:
        isort(l,k-1)
        insert(l,k-1)
def insert(l,k):
    pos=k
    while pos>0 and l[pos]<l[pos-1]:
        l[pos],l[pos-1]=l[pos-1],l[pos]
        pos-=1
l=list(range(4,4000,2))
from random import shuffle
shuffle(l)
print(l)
isort(l, len(l))
print(l)
print(insertion_sort_recursive(l))