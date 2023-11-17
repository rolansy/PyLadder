n=int(input())
l=[]
for i in range(n):
    l1=[]
    m=int(input())
    for i in range(m):
        x=int(input())
        l1.append(x)
    l1.reverse()
    l.append(l1)
for i in l:
    for j in i:
        print(j)