def gcd(m,n):
    m,n=max(m,n),min(m,n)
    
    if m%n==0:
        return n
    else:
        d=m-n
        return(gcd(max(n,d),min(n,d)))
m=int(input("Enter First Number : "))
n=int(input("Enter Second Number : "))
print("GCD : ",gcd(m,n))