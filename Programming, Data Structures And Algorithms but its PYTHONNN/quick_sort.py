# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:22:08 2024

@author: ronal
"""

def quicksort(a,l,r):
    if r-l<=1:  #base
        return ()
    yellow=l+1
    
    for green in range(l+1,r):
        if a[green]<=a[l] :  #pivot=a[l]
            a[green],a[yellow]=a[yellow],a[green]
            yellow+=1
    
    #move pivot to place
    a[l],a[yellow-1]=a[yellow-1],a[l]
    quicksort(a, l, yellow-1)
    quicksort(a, yellow, r)
    return a

#l=list(range(4,90000,3)) 
l=list(range(4,300,4))
from random import shuffle
shuffle(l)
#l.sort(reverse=True)
print(l)
q=quicksort(l, 0, len(l))
print(q)
    