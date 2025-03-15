import math
import os
import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(q):
    primes = []
    num = 2
    while len(primes) < q:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def waiter(number, q):
    primes = generate_primes(q)
    result = []
    for i in range(q):
        A = []
        B = []
        while number:
            plate = number.pop()
            if plate % primes[i] == 0:
                B.append(plate)
            else:
                A.append(plate)
        result.extend(B[::-1])
        number = A
    result.extend(number[::-1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()