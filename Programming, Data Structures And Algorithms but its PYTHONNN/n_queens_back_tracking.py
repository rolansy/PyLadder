# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:57:51 2024

@author: ronal
"""

def placequeen(i,board):
    n=len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i==n-1:
                return True
            else:
                extendsoln=placequeen(i+1, board)
            if extendsoln:
                return True
            else:
                undoqueen(i,j,board)
        else:
            return False
board={}
n=int(input("How Many Queens? : "))
if placequeen(0, board):
    print('board')
    