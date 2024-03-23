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
    