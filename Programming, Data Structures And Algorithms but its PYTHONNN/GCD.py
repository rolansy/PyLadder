m=int(input("Enter First Number : "))
n=int(input("Enter Second Number : "))
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            xgcd=i
    return (xgcd)
        
print("GCD of ",m," and ",n," is : ",gcd(m,n))