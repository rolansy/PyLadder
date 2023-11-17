def excrate(n):
    n = list(str(n))
    lenn = len(n)
    lastd = n[lenn-1]
    idx = -1

    for i in range(lenn-2, -1, -1):
        if int(n[i]) % 2 == 0:
            idx = i
            if n[i] < lastd:
                break

    if idx != -1:
        n[lenn-1], n[idx] = n[idx], n[lenn-1]
        return int(''.join(n))
    else:
        return -1
n=input()
print(excrate(n))