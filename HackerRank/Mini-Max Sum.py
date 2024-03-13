#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    l=[]
    for i in range(len(arr)):
        d=0
        for j in range(len(arr)):
            if j!=i:
                d+=arr[j]
        l.append(d)
    print(min(l),max(l),sep=" ")
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
