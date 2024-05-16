# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:26:16 2024

@author: ronal
"""
x='y'
while x.lower()!='n':
    try:
        n=int(input("Input First Number : "))
        m=int(input("Input Second Number : "))
        print("Quotioent : ",n/m)
    except ZeroDivisionError:
        print("0 div not possible")
    else:
        x=input("Continue [y/n]: ")
        
        