#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndMinimax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER p
#  3. INTEGER q
#

def sherlockAndMinimax(arr, p, q):
    # Write your code here
    d={}
    for i in list(range(p,q+1)):
        d[i]=None
    for i in list(range(p,q+1)):
        x=[]
        for j in arr:
            x.append(abs(j-i))
            d[i]=min(d[i],abs(j-i))
        d[i]=min(x)
    return(list(d.keys())[list(d.values()).index(max(list(d.values())))])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
