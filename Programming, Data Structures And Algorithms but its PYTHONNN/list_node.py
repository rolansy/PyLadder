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
        return
    
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
    
    def insert(self,v):
        if self.isempty():
            self.value=v
            return
        newnode=Node(v)
        self.value,newnode.value=newnode.value,self.value
        self.next,newnode.next=newnode,self.next
        return
    
    def delete(self,v):
        if self.isempty():
            print("Empty")
            return
        if self.value==v:
            if self.next==None:
                self.value=None
                return
            else:
                self.value=self.next.value
                self.next=self.next.next
                return
                
        temp=self
        while temp.next!=None:
            if temp.next.value==v:
                temp.next=temp.next.next
                return
            else:
                temp=temp.next
        
        return
    
    def deleter(self,v):
        if self.isempty():
            print("Empty")
            return
        if self.value==v:
            if self.next==None:
                self.value=None
                return
            else:
                self.value=self.next.value
                self.next=self.next.next
                return
        
        if self.next!=None:
            self.next.deleter(v)
            if self.next.value==None:
                self.next=self.next.next
        return
        
    def __str__(self):
        selflist=[]
        
        if self.value==None:
            return(str(selflist))
        temp=self
        selflist.append(temp.value)
        while temp.next!=None:
            temp=temp.next
            selflist.append(temp.value)
        return(str(selflist))
    
    
    