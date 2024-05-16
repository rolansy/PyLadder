# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:14:12 2024

@author: ronal
"""
from math import sqrt

class Point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
        
    def translate(self,deltax,deltay):
        self.x+=deltax
        self.y+=deltay
    
    def odistance(self):
        return(sqrt(self.x**2+self.y**2))
    def __str__(self):
        return('('+str(self.x)+','+str(self.y)+')')
    
    
class rpoint:
    def __init__(self,a=1,b=1):
        self.r=sqrt(a**2+b**2)
        if a==0:
            self.theta=0
        else:
            self.theta=b/a #atan(b/a)
    
    def odistance(self):
        return self.r