# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:07:36 2024

@author: ronal
"""

class Node:
    def __init__(self,initval=None):
        self.value=initval
        self.next=None
    
    def isempty(self):
        return(self.value==None)
    
    def append(self,v):
        if self.isempty():
            self.value=v
        elif self.next==None:
            newnode=Node(v)
            self.next=newnode
        else:
            (self.next).append(v)
        return
    
    def appendi(self,v):
        if self.isempty():
            self.value=v
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        newnode=Node(v)
        temp.next=newnode
        return()
    
    def printi(self):
        if self.isempty():
            print("Empty")
            return
        temp=self
        while temp!=None:
            print(temp.value,"->",end="")
            temp=temp.next
        print("x")
        return
        
    
    
    