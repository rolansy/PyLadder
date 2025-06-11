def kaprekarNumbers(p, q):
    found = False
    for n in range(p, q+1):
        d = len(str(n))
        sq = str(n * n)
        r = int(sq[-d:]) if sq[-d:] else 0
        l = int(sq[:-d]) if sq[:-d] else 0
        if l + r == n:
            print(n, end=' ')
            found = True
    if not found:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
