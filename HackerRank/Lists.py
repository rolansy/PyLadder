if __name__ == '__main__':
    n = int(input())
    l=[]
    for i in range(n):
        x=list(input().split())
        if x[0]=='insert':
            l.insert(int(x[1]),int(x[2]))
        elif x[0]=='remove':
            l.remove(int(x[1]))
        elif x[0]=='print':
            print(l)
        elif x[0]=='pop':
            l.pop()
        elif x[0]=='reverse':
            l.reverse()
        elif x[0]=='sort':
            l.sort()
        elif x[0]=='append':
            l.append(int(x[1]))