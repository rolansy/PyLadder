
def mergesort(l,left,right):
    if right-left<=1: #base
        return l[left:right]
    #recursive
    mid=(left+right)//2
    L=mergesort(l,left,mid)
    R=mergesort(l, mid, right)
    
    return merge(L,R)
def merge(a,b):  #merging a and b into c
    c=[]
    m,n=len(a),len(b)
    i,j=0,0
    while i+j<m+n:
        if i==m:
            c+=b[j:]
            j+=len(b)-j
            #c.append(b[j])
            #j+=1
        elif j==n:
            c+=a[i:]
            i+=len(a)-i
            #c.append(b[i])
            #i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
    return c

#print(merge([2,3,7,9],[1,3,5,8,9,12,34,56,78,99]))
from random import shuffle
l=list(range(4,200000,3))
shuffle(l)
l.sort(reverse=True)
m=mergesort(l,0,len(l))
print(m)

