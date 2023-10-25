
a=list(range(1,30000))

def bins(a,x):
    top=0
    end=len(a)-1
    f=0
    c=0
    while(top<end and f==0):
        c+=1
        mid=(top+end)//2
        if x==a[mid]:
            f=1
            print("Element Found At : ",mid)
            print("The Number of Iterations are : ",c)
            return
        elif x<a[mid]:
            end=mid-1
        else: 
            top=mid+1
    print("Not Found")
bins(a, 25)