n = int(input())
arr = map(int, input().split())

d={}
for i in arr:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(sorted(d)[-2])
    