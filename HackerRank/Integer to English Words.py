#!/bin/python3

import os

def numToWords(num):
    if num == 0:
        return "Zero"
    
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return below_20[n // 100] + " Hundred " + helper(n % 100)
    
    res = ""
    for i, chunk in enumerate(thousands):
        if num % 1000 != 0:
            res = helper(num % 1000) + chunk + " " + res
        num //= 1000
    
    return res.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = numToWords(n)

    fptr.write(k + '\n')

    fptr.close()