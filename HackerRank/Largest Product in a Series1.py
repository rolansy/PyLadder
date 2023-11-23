t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    l=[0]
    for i in range(n-k):
        p=1
        for j in range(i,i+k):
            p=p*int(s[j])
        l.append(p)
    print(max(l))      
    
