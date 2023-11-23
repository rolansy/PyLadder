import math

def encryption(s):
    s = s.replace(' ', '')
    L = len(s)
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    if rows * cols < L:
        rows += 1

    encoded = ''
    for i in range(cols):
        for j in range(i, L, cols):
            encoded += s[j]
        encoded += ' '

    return encoded.strip()

s = input()
print(encryption(s))