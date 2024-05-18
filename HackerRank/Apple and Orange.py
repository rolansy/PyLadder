def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    x=0
    y=0
    apples=[a+i for i in apples]
    oranges=[b+i for i in oranges]
    for i in apples:
        if i in range (s,t+1):
            x+=1
    for j in oranges:
        if j in range(s,t+1):
            y+=1
        
    print(x,y,sep="\n")