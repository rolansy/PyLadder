m=int(input("Enter First Number : "))
n=int(input("Enter Second Number : "))
a=[]
b=[]
for i in range(1,m+1):
    if m%i==0:
        a.append(i)
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
x=[]
for i in a:
    if i in b:
        x.append(i)
        
print("GCD of ",m," and ",n," is : ",max(x))