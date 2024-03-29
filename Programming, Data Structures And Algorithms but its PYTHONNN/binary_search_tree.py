# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:08:22 2024

@author: ronal
"""

class tree:
    def __init__(self,initval=None):
        self.value=initval
        if self.value:
            self.left=tree()
            self.right=tree()
        else:
            self.left=None
            self.right=None
        return
    
    def isempty(self):
        return self.value==None
    
    def inorder(self):
        if self.value==None:
            return([])
        if self.isempty():
            return([])
        return(self.left.inorder()+[self.value]+self.right.inorder())
        
    def __str__(self):
        return(str(self.inorder()))
    
    def find(self,v):
        if self.isempty():
            return False
        if self.value==v:
            return True
        if v<self.value:
            return self.left.find(v)
        return self.right.find(v)
    
    def minval(self):
        if self.left==None:
            return(self.value)
            
        return self.left.minval()
    
    def maxval(self):
        if self.right==None:
            return (self.value)
        return self.right.maxval()
    
    def insert(self,v):
        
        if self.isempty():
            self.value=v
            self.left=tree()
            self.right=tree()
            
        if self.value==v:
            return
        
        if v<self.value:
            self.left.insert(v)
            return
        self.right.insert(v)
        return
    
    def delete(self,v):
        if self.isempty():
            print("Empty")
            return
        if v<self.value:
            v.left.delete(v)
            return
        if v>self.value:
            v.right.delete(v)
            return
        
        if v==self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value=self.left.maxval()
                self.left.delete((self.left.maxval()))
            return
    
    
    
    
    