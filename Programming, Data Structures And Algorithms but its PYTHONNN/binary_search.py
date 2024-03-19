# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:24:30 2024

@author: ronal
"""

def bsearch(v,seq,l,r):
    if r-l==0:
        return False
    mid=(l+r)//2
    if seq[mid]==v:
        print(v,"found at ",mid)
        return True
    if v>seq[mid]:
        return bsearch(v, seq, mid, r)
    elif v<seq[mid]:
        return bsearch(v, seq, l, mid)
    
seq=(list(map(int,input("Enter Sequence : ").split())))
v=int(input("Enter Value to be searched : "))
print(bsearch(v, seq, 0, len(seq)))
