# -*- coding: utf-8 -*-
"""
Created on Wed May 15 21:40:46 2024

@author: ronal
"""

def base(n,b):
        x=n
        s=""
        while x>0:
           s=str(x%b)+s
           x=x//b
        return s
p=base(9,2)
print(p)
def pal(p):
    if p==p[::-1]:
        return True
    return False
print(pal(p))

def isStrictlyPalindromic( n):
        for i in range(2,n-1):
            x=n
            s=""
            while x>0:
                s=str(x%i)+s
                x=x//i
            if s!=s[::-1]:
                return False
        return True

i=4
while True:
    if isStrictlyPalindromic(i):
        print (True,i)
    i+=1