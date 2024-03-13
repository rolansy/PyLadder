if __name__ == '__main__':
    l=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append(score)
        l.append([name,score])
    s.sort()
    i=0
    while s[i]==s[i+1]:
        i+=1
    sl=s[i+1]
    std=[]
    for i in l:
        if i[1]==sl:
            std.append(i[0])
    
    std.sort()
    for i in std:
        print (i)
    
    
