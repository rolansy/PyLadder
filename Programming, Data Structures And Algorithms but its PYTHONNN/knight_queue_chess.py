# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:31:16 2024

@author: ronal
"""

def explore((sx,sy),(tx,ty)):
    marked=[[0 for i in range(n)] for j in range(m)]
    marked[sx][sy]=1
    queue=[(sx,sy)]
    while queue!=0:
        (ax,ay)=queue.pop()
        for (nx,ny) in neighbours((ax,ay)):
            if !marked[nx][ny]:
                marked[nx][ny]=1
                queue.insert(0, (nx,ny))
    return(marked[tx][ty])