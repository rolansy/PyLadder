m=int(input("Enter First Number : "))
n=int(input("Enter Second Number : "))
def gcd(m,n):
    for i in range(min(m,n),0,-1):
        if m%i==0 and n%i==0:
            return(i)

print("GCD of ",m," and ",n," is : ",gcd(m,n))