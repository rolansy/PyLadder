# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:48:21 2024

@author: ronal
"""

def balancedSums(arr):
    # Write your code here
    n=len(arr)
    for  i in range(len(arr),-1,-1):
        if sum(arr[:i])==sum(arr[i+1:]):
            return ('YES')
    return 'NO'        
print(balancedSums([5,6,8,11]))