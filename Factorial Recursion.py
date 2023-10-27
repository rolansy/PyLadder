def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)

n=int(input("Enter Number to Find Factorial of : "))
print("Factorial : ",f(n))
