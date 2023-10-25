def lins(a,x):
    for i in a:
        if i==x:
            print("Found",i,"at position : ",x)

a=list(range(1,1000))

lins(a,500)