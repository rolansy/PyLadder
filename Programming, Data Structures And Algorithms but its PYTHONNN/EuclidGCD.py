def gcdr(m,n): #using recursion
    m,n=max(m,n),min(m,n)
    
    if m%n==0:
        return n
    else:
        d=m-n
        return(gcdr(max(n,d),min(n,d)))
    
def gcd(m,n):
    m,n=max(m,n),min(m,n)
    while m%n!=0:
        d=m-n
        m,n=max(n,d),min(n,d)
    return n

def euclidgcdr(m,n):
    m,n=max(m,n),min(m,n)
    if m%n==0:
        return n
    else:
        return (gcdr(n,m%n)) #m%n=remainder
def euclidgcd(m,n):
    m,n=max(m,n),min(m,n)
    while m%n!=0:
        m,n=n,m%n
    return n
    
    
m=int(input("Enter First Number : "))
n=int(input("Enter Second Number : "))
print("GCD with recursion : ",gcdr(m,n))
print("GCD with while (no recursion) : ",gcd(m,n))
print("Euclid's Algo GCD with recursion : ",euclidgcdr(m, n))
print("Euclid's Algo GCD with while (no recursion) : ",euclidgcdr(m, n))