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