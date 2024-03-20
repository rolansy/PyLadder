def merge(a,b):
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
            j+=len(a)-i
            #c.append(b[i])
            #i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
    return c

