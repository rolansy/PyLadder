# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:32:44 2024

@author: ronal
"""

import numpy as np
a=[[1,2],[2,1]]
print(a)
print(np.linalg.det([[1,2],[2,1]]))
vals,vecs=np.linalg.eig(a)
print(vals,vecs,sep="\n")
print(np.linalg.inv(a))

n=int(input())
a=[]
for i in range(n):
    c=list(map(float,input().split()))
    a.append(c)

print(np.linalg.det(a).round(2))

