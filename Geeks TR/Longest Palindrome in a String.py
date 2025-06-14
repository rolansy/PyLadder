# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:37:37 2024

@author: ronal
"""

def pal(st):
    if st==st[::-1]:
        return True
    return False

def longestPalin(S):
        # code here
        n=f=len(S)
        global st
        while n!=-1:
            for i in range(f-n):
                st=str(S[i:n+i+1])
                print(st,n)
            if st==st[::-1]:
                return st
            n-=1
S="indad"
longestPalin(S)