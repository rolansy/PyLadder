import random
def lins(a,x):
    f=0
    c=0
    for i in a:
        if i==x:
            c+=1
            print("Found",i,"at position : ",x)
            f=1
    if f==1:
        print("Number of Occurunces : ",c)
    else:
        print("Not Found")

a=[]
for i in range(1,1000):
    a.append(random.randint(1,100))
lins(a,56)