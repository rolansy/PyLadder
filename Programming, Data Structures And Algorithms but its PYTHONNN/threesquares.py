def threesquares(m):
    for i in range(0,m//2):
        for j in range(0,m//2):
            for k in range(0,m//2):
                if (i**2+j**2+k**2)==m:
                    return True
    return False
print(threesquares(6))