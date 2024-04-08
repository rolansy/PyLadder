# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 02:32:52 2024

@author: ronal
"""
fibtable={}

def mem_fib(n):
    if n in fibtable.keys():
        return (fibtable[n])
    if n==0 or n==1:
        value=n
    else:
        value=mem_fib(n-1)+mem_fib(n-2)
    fibtable[n]=value
    print(value)
    return value
 
def fib(n):
    if n in [0,1]:
        value=n
    else:
        value=fib(n-1)+fib(n-2)
    print(value)
    return value

def dyn_fib(n):
    fibtable[0]=0
    fibtable[1]=1
    for i in range(2,n+1):
        fibtable[i]=fibtable[i-1]+fibtable[i-2]
    return(fibtable[n])