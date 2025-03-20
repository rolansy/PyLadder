def maxProfit(prices):
    l=prices
    n=len(l)
    i=1
    p=0
    x=l[0]
    mx=0
    while i<n:
        if l[i]>x:
            p=l[i]-x
        else:
            p=0
            x=l[i]
        mx=max(mx,p)
        i+=1   
    return(mx)