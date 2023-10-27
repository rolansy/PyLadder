# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:32:14 2023

@author: ronal
"""

import numpy
a=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
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
    
def checkr(s):
    for r in range(3):
        c=0
        for c in range(3):
            if a[r][c]==s:
                c+=1
        if c==3:
            print(s,"won!")
            return True
    return False
    
def checkc(s):
    for c in range(3):
        c=0
        for r in range(3):
            if a[r][c]==s:
                c+=1
        if c==3:
            print(s,"won!")
            return True
    return False    
    
def checkd(s):
    if a[0][2]==a[1][1] and a[1][1]==a[2][0] and a[1][1]==s:
        print(s,"won!")
        return True
    if a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[1][1]==s: 
        print(s,"won!")
        return True
    return False

def won(s):
    return checkr(s) or checkc(s) or checkd(s)

def play():
    for turn in range(9):
        if turn%2==0:
            print("turn of ",p1)
            place(p1)
            if won(p1):
                print(numpy.matrix(a))
                break
        else:
            print("turn of ",p2)
            place(p2)
            if won(p2):
                print(numpy.matrix(a))
                break
        if not(won(p1)) and not(won(p2)):
            print(numpy.matrix(a))
            print("Draw")


play()