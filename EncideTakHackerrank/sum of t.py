t=int(input())
for i in range(t):
    n = list(map(int, input().split()))
    s=0
    for i in range(len(n)):
        s+=n[i]
    print(s)