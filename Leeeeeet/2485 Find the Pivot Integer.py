def pivotInteger(n):
    if n==1:
        return 1
    l=list(range(1,n+1))
    for i in range(1,n+1):
        if sum(l[:i])==sum(l[i-1:]):
            return i
    return -1
print(pivotInteger(8))