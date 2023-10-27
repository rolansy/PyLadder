# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:32:14 2023

@author: ronal
"""

import numpy
a=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(a)
p1='X'
p2='O'
def place(s): 
    print(numpy.matrix(a))
    while(1):
        r=int(input("Enter Row [1/2/3]: "))
        c=int(input("Enter Column [1/2/3]: "))
        if r in [1,2,3] and c in [1,2,3] and a[r-1][c-1]=='-':
            break
        else:
            print("Invalid Input. Enter Again")
    a[r-1][c-1]=s

def play():
    for turn in range(9):
        if turn%2==0:
            print("turn of ",p1)
            place(p1)
            if won(p1):
                break
        else:
            print("turn of ",p2)
            place(p2)
            if won(p2):
                break


play