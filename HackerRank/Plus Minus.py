#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    d={1:0,2:0,3:0}
    for i in arr:
        if '-' in str(i):
            d[2]+=1
        elif i==0:
            d[3]+=1
        else:
            d[1]+=1
    for i in d.keys():
        print(d[i]/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
