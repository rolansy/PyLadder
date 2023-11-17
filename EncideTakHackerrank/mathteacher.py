def mathteach(t,n):
    try:
        t=int(input())
        if t<0 or t>10000:
            print("error")
            return
        d={}
        l=[]
        n = list(map(int, input().split()))
        for i in n:
            if i<2 or i>10000:
                print("error")
                return
                
            l.append(i)
        s=0
        for i in l:
            s+=i
        av=s/t
        c=0
        for i in l:
            if i<av:
                c+=1
        print(c)
        return t,n
    except:
        print("error")
        return
    
t=n=0
t,n=mathteach(t,n)