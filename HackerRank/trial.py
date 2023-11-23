n=int(input())
l=[]
d={}
for i in range(n):
    l.append(input())
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(len(d.keys()))
for i in d.keys():
    print(d[i],end=" ")
    